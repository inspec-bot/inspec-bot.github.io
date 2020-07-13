sudo apt-get install python-dev
sudo apt-get install python-rpi.gpio
sudo apt-get install python-smbus i2c-tools

sudo nano /boot/config.txt
dtparam=i2c_arm=on
dtparam=i2s=on

sudo nano /etc/modules
i2c-bcm2708
i2c-dev

sudo reboot

mkdir motor-hat
cd motor-hat
wget https://raw.githubusercontent.com/inspecbot/inspecbot.github.io/master/pi/pi-motor-hat.zip
unzip pi-motor-hat.zip

#check address I2C> sudo i2cdetect -y 1

# Enable I2C
ref~
- https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c
