#!/usr/bin/python
from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor

import time
import atexit

# create a default object, no changes to I2C address or frequency
mh = Raspi_MotorHAT(addr=0x6f)

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
	mh.getMotor(1).run(Raspi_MotorHAT.RELEASE)
	mh.getMotor(2).run(Raspi_MotorHAT.RELEASE)
	mh.getMotor(3).run(Raspi_MotorHAT.RELEASE)
	mh.getMotor(4).run(Raspi_MotorHAT.RELEASE)

atexit.register(turnOffMotors)

# DC motor test!
myMotor1 = mh.getMotor(3)
myMotor2 = mh.getMotor(4)

# set the speed to start, from 0 (off) to 255 (max speed)
# 40/80 min (unbalance motor)
myMotor1.setSpeed(150)
myMotor2.setSpeed(150)
# turn on motor
myMotor1.run(Raspi_MotorHAT.RELEASE);
myMotor2.run(Raspi_MotorHAT.RELEASE);
