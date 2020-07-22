`sudo nano /etc/wpa_supplicant/wpa_supplicant.conf`</br>

network={</br>
    ssid="testing"</br>
    psk="testingPassword"</br>
}

## RTL8188EUS
check kernel > uname -a
http://downloads.fars-robotics.net/wifi-drivers/8188eu-drivers/
mkdir 8188eu
cd 8188eu
wget http://downloads.fars-robotics.net/wifi-drivers/8188eu-drivers/8188eu-4.19.118-v7-1311.tar.gz
tar xzf 8188eu-4.19.118-v7-1311.tar.gz
./install.sh
sudo reboot
