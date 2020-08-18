ref: https://www.pyimagesearch.com/2019/04/15/live-video-streaming-over-network-with-opencv-and-imagezmq/
pip3 install opencv-contrib-python==4.1.0.25
***Not use*** [pip3 install opencv-contrib-python]
pip3 install imagezmq
pip3 install imutils

// MobileNet-SSD source
https://github.com/chuanqi305/MobileNet-SSD
wget https://raw.githubusercontent.com/inspecbot/inspecbot.github.io/master/pi/cam/MobileNetSSD_deploy.caffemodel
wget https://raw.githubusercontent.com/inspecbot/inspecbot.github.io/master/pi/cam/MobileNetSSD_deploy.prototxt
wget https://raw.githubusercontent.com/inspecbot/inspecbot.github.io/master/pi/cam/client.py


// for client
python3 client.py --server-ip 192.168.137.1
