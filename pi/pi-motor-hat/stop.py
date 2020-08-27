#!/usr/bin/python
from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor

import time
import atexit

mh = Raspi_MotorHAT(addr=0x6f)

mh.getMotor(1).run(Raspi_MotorHAT.RELEASE)
mh.getMotor(2).run(Raspi_MotorHAT.RELEASE)
mh.getMotor(3).run(Raspi_MotorHAT.RELEASE)
mh.getMotor(4).run(Raspi_MotorHAT.RELEASE)
