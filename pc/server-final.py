from imutils import build_montages
from datetime import datetime
import numpy as np
import imagezmq
import argparse
import imutils
import cv2
import paramiko
import time
import threading
import requests
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--prototxt", required=True,
    help="path to Caffe 'deploy' prototxt file")
ap.add_argument("-m", "--model", required=True,
    help="path to Caffe pre-trained model")
ap.add_argument("-c", "--confidence", type=float, default=0.2,
    help="minimum probability to filter weak detections")
ap.add_argument("-mW", "--montageW", required=True, type=int,
    help="montage frame width")
ap.add_argument("-mH", "--montageH", required=True, type=int,
    help="montage frame height")
args = vars(ap.parse_args())
imageHub = imagezmq.ImageHub()
CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
     "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
     "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
     "sofa", "train", "tvmonitor"]
print("[INFO] loading model...")
net = cv2.dnn.readNetFromCaffe(args["prototxt"], args["model"])
CONSIDER = set(["person"])
objCount = {obj: 0 for obj in CONSIDER}
frameDict = {}
lastActive = {}
lastActiveCheck = datetime.now()
ESTIMATED_NUM_PIS = 1
ACTIVE_CHECK_PERIOD = 40
ACTIVE_CHECK_SECONDS = ESTIMATED_NUM_PIS * ACTIVE_CHECK_PERIOD
mW = args["montageW"]
mH = args["montageH"]
print("[INFO] detecting: {}...".format(", ".join(obj for obj in
    CONSIDER)))
statusX = 0
pzz = paramiko.SSHClient()
pzz.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
pzz.connect("192.168.137.x", port=22, username="pi", password="password")
pzz.exec_command("python3 client2.py --server-ip 192.168.137.x &")
statusY = 0
dropY = 0
secX =  0
secY =  1
secYO = 1
indexX = 0
cenX = 0
sizeX = 2
indexS = 0
indexL = 0
indexR = 0
indexLX1 = 0
indexLX2 = 0
indexRX1 = 0
indexRX2 = 0
indexB1 = 0
indexF1 = 0
indexF2 = 0
def dStop():
    indexS = 1
    stdin, stdout, stderr = pzz.exec_command("python ./motor-hat/stop.py")
    indexS = 0
def dLeftx1():
    indexLX1 = 1
    stdin, stdout, stderr = pzz.exec_command("python ./motor-hat/left-x1.py")
    time.sleep(0.2)
    indexLX1 = 0
def dLeftx2():
    indexLX2 = 1
    stdin, stdout, stderr = pzz.exec_command("python ./motor-hat/left-x2.py")
    time.sleep(0.2)
    indexLX2 = 0
def dRightx1():
    indexRX1 = 1
    stdin, stdout, stderr = pzz.exec_command("python ./motor-hat/right-x1.py")
    time.sleep(0.2)
    indexRX1 = 0
def dRightx2():
    indexRX2 = 1
    stdin, stdout, stderr = pzz.exec_command("python ./motor-hat/right-x2.py")
    time.sleep(0.2 )
    indexRX2 = 0
def dRight1():
    indexR = 1
    stdin, stdout, stderr = pzz.exec_command("python ./motor-hat/right1.py")
    time.sleep(0.2)
    indexR = 0
def dLeft1():
    indexL = 1
    stdin, stdout, stderr = pzz.exec_command("python ./motor-hat/left1.py")
    time.sleep(0.2)
    indexL = 0
def dBack1():
    indexB1 = 1
    stdin, stdout, stderr = pzz.exec_command("python ./motor-hat/back1.py")
    time.sleep(0.6)
    indexB1 = 0
    print("B1",secX,secY)
def dFor1():
    indexF1 = 1
    stdin, stdout, stderr = pzz.exec_command("python ./motor-hat/for1.py")
    time.sleep(0.6)
    indexF1 = 0
    print("F1",secX,secY)
def dFor2():
    indexF2 = 1
    stdin, stdout, stderr = pzz.exec_command("python ./motor-hat/for2.py")
    time.sleep(2)
    indexF2 = 0
    print("F2",secX,secY)
while True:
    (rpiName, jpg_buffer) = imageHub.recv_jpg()
    image = cv2.imdecode(np.frombuffer(jpg_buffer, dtype='uint8'), -1)
    imageHub.send_reply(b'OK')
    if rpiName not in lastActive.keys():
        print("[INFO] receiving data from {}...".format(rpiName))
    lastActive[rpiName] = datetime.now()
    frame = image
    (h, w) = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 0.007843, (300, 300), 127.5)
    net.setInput(blob)
    detections = net.forward()
    objCount = {obj: 0 for obj in CONSIDER}
    for i in np.arange(0, detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > args["confidence"]:
            idx = int(detections[0, 0, i, 1])
            if CLASSES[idx] in CONSIDER:
                objCount[CLASSES[idx]] += 1
                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX, startY, endX, endY) = box.astype("int")
                cv2.rectangle(frame, (startX, startY), (endX, endY), (255, 0, 0), 2)
                statusYO = statusY
                dropYO = dropY
                if startY < 80:
                    statusY = 1
                if startY >= 80 and startY < 160:
                    statusY = 2
                if startY >= 160 and startY < 240:
                    statusY = 3
                if startY >= 240 and startY < 320:
                    statusY = 4
                if startY >= 320 and startY < 400:
                    statusY = 5
                if startY >= 400 and startY < 480:
                    statusY = 6
                if statusY > statusYO:
                    dropY = dropY + (statusY - statusYO)
                if statusY < statusYO:
                    dropY = 0
                if dropY >= 3 and dropY != dropYO:
                    print("Drop!!")
                    urlMain = "http://192.168.137.100/drop"
                    URL = urlMain
                    r = requests.get(url = URL)
                secYO = secY
                if startY < 20:
                    secY = 1
                if startY >= 20 and startY < 50:
                    secY = 2
                if startY >= 50 and startY < 140:
                    secY = 3
                if startY >= 140:
                    secY = 4
                sizeXO = sizeX
                sizeX = endX - startX
                if sizeX < 240:
                    szX = 1
                if sizeX >= 240:
                    szX = 2
                secXO = secX
                cenX = startX / 2 + endX / 2
                if cenX < 260:
                    secX = 1
                    if endX < 350:
                        if szX == 1:
                            secX = 11
                        if szX == 2:
                            secX = 12
                if cenX >= 260 and cenX < 380:
                    secX = 2
                if cenX  >= 380:
                    secX = 3
                    if startX > 290:
                        if szX == 1:
                            secX = 31
                        if szX == 2:
                            secX = 32
                if startX < 10 and endX < 380:
                    secX = 12
                if endX > 630 and startX > 260:
                    secX = 32
                if secX != secXO and secY != secYO:
                    print(secX,secY)
                if secX != 2:
                    if secX == 11 and indexLX1 == 0:
                        mLeftx1 = threading.Thread(target=dLeftx1)
                        mLeftx1.start()                      
                    if secX == 12 and indexLX2 == 0:
                        mLeftx2 = threading.Thread(target=dLeftx2)
                        mLeftx2.start()
                    if secX == 31 and indexRX1 == 0:
                        mRightx1 = threading.Thread(target=dRightx1)
                        mRightx1.start()
                    if secX == 32 and indexRX2 == 0:
                        mRightx2 = threading.Thread(target=dRightx2)
                        mRightx2.start()
                    if secX == 1 and indexL == 0:
                        mLeft1 = threading.Thread(target=dLeft1)
                        mLeft1.start()
                    if secX == 3 and indexR == 0:
                        mRight1 = threading.Thread(target=dRight1)
                        mRight1.start()
                if secX == 2:
                    if indexS == 0 and secXO != secX:
                        mStop = threading.Thread(target=dStop)  
                        mStop.start()
                    if secY == 1 and indexB1 == 0:
                        mBack1 = threading.Thread(target=dBack1)  
                        mBack1.start()
                    if secY == 3 and indexF1 == 0:
                        mFor1 = threading.Thread(target=dFor1)  
                        mFor1.start()
                    if secY == 4 and indexF2 == 0:
                        mFor2 = threading.Thread(target=dFor2)
                        mFor2.start()
                    if secY == 2 and indexS == 0:
                        mStop = threading.Thread(target=dStop)  
                        mStop.start()
    cv2.putText(frame, rpiName, (10, 25),
        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    label = ", ".join("{}: {}".format(obj, count) for (obj, count) in
        objCount.items())
    cv2.putText(frame, label, (10, h - 20),
        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255,0), 2)
    frameDict[rpiName] = frame
    montages = build_montages(frameDict.values(), (w, h), (mW, mH))
    for (i, montage) in enumerate(montages):
        cv2.imshow("OpenCV tracking ({})".format(i),
            montage)
    key = cv2.waitKey(1) & 0xFF
    if (datetime.now() - lastActiveCheck).seconds > ACTIVE_CHECK_SECONDS:
        for (rpiName, ts) in list(lastActive.items()):
            if (datetime.now() - ts).seconds > ACTIVE_CHECK_SECONDS:
                print("[INFO] lost connection to {}".format(rpiName))
                lastActive.pop(rpiName)
                frameDict.pop(rpiName)
        lastActiveCheck = datetime.now()
    if key == ord("q"):
        pzz.exec_command(" pkill -9 -f client2.py")
        pzz.exec_command(" python ./motor-hat/stop.py")
        break
cv2.destroyAllWindows()
