#!/usr/bin/python
from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor

import time
import atexit

mh = Raspi_MotorHAT(addr=0x6f)

# recommended for auto-disabling motors on shutdown!
#def turnOffMotors():
#	mh.getMotor(1).run(Raspi_MotorHAT.RELEASE)
#	mh.getMotor(2).run(Raspi_MotorHAT.RELEASE)
#	mh.getMotor(3).run(Raspi_MotorHAT.RELEASE)
#	mh.getMotor(4).run(Raspi_MotorHAT.RELEASE)
#atexit.register(turnOffMotors)

# motor-config
myMotor1 = mh.getMotor(1)
myMotor2 = mh.getMotor(3)

# set speed 0 (off) to 255 (max speed) 256/x-1
# 40-? min (unbalance motor)

myMotor1.setSpeed(127)
myMotor2.setSpeed(127)
myMotor1.run(Raspi_MotorHAT.RELEASE);
myMotor2.run(Raspi_MotorHAT.RELEASE);
myMotor1.run(Raspi_MotorHAT.FORWARD)
myMotor2.run(Raspi_MotorHAT.BACKWARD)
time.sleep(0.01)

myMotor1.setSpeed(47)
myMotor2.setSpeed(47)
myMotor1.run(Raspi_MotorHAT.FORWARD)
myMotor2.run(Raspi_MotorHAT.BACKWARD)
