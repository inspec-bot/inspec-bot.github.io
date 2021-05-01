from imutils.video import VideoStream
import imagezmq
import argparse
import socket
import time
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-s", "--server-ip", required=True,
        help="ip address of the server to which the client will connect")
args = vars(ap.parse_args())

sender = imagezmq.ImageSender(connect_to="tcp://{}:5555".format(
        args["server_ip"]))

rpiName = socket.gethostname()
vs = VideoStream(usePiCamera=True, resolution=(640, 480)).start()
time.sleep(2.0)
jpeg_quality = 80
while True:
        image = vs.read()
        ret_code, jpg_buffer = cv2.imencode(
            ".jpg", image, [int(cv2.IMWRITE_JPEG_QUALITY), jpeg_quality])
        sender.send_jpg(rpiName, jpg_buffer)
