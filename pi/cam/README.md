sudo raspi-config
> enable cam

ref: https://www.pyimagesearch.com/2019/04/15/live-video-streaming-over-network-with-opencv-and-imagezmq/
pip3 install opencv-contrib-python==4.1.0.25
***Not use*** [pip3 install opencv-contrib-python]
pip3 install imagezmq
pip3 install imutils
sudo apt-get install libatlas-base-dev
sudo apt-get install libhdf5-dev
sudo apt-get install libjasper-dev
sudo apt-get install libharfbuzz-dev
sudo apt-get install libilmbase-dev
sudo apt-get install libopenexr-dev
sudo apt-get install libgstreamer1.0-dev
sudo apt-get install python3-picamera
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
sudo apt-get install libqtgui4 
sudo apt-get install libqt4-test

// MobileNet-SSD source
https://github.com/chuanqi305/MobileNet-SSD
wget https://raw.githubusercontent.com/inspecbot/inspecbot.github.io/master/pi/cam/MobileNetSSD_deploy.caffemodel
wget https://raw.githubusercontent.com/inspecbot/inspecbot.github.io/master/pi/cam/MobileNetSSD_deploy.prototxt
wget https://raw.githubusercontent.com/inspecbot/inspecbot.github.io/master/pi/cam/client.py


// for client
python3 client.py --server-ip 192.168.137.1
