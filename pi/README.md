
# Pi part

## Installation

- install raspbian lite to sdcard / download ref: https://www.raspberrypi.org/downloads/raspberry-pi-os/
- enable ssh by create `ssh` file in boot partition
- pi default pass `pi : raspberry` / chang pass by `passwd`
- update pi </br>
`sudo apt-get update`
`sudo apt-get upgrade`
- config by `raspi-config` </br>
`- set time`
`- set time`
`- set time`
`- set time`
- install python </br>
`sudo apt-get install -y build-essential tk-dev libncurses5-dev libncursesw5-dev libreadline6-dev libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev libffi-dev tar wget` </br>
`wget https://www.python.org/ftp/python/3.8.3/Python-3.8.3.tgz` </br>
`sudo tar zxf Python-3.8.3.tgz` </br>
`cd Python-3.8.3` </br>
`sudo ./configure --enable-optimizations` </br>
`sudo make -j 4` </br>
`sudo make altinstall` </br>

## Usage

instructions </br>test
