import network #! Library ที่ Import มาต้องไปลองใน Thonny อีกรอบ
import socket 
from simple import MQTTClient
from neopixel import NeoPixel
import dht
import json
import machine
import time
from machine import Pin, PWM
from machine import *
from hcsr04 import HCSR04
from ServoLib import Servo
button4 = Pin(4, Pin.IN, Pin.PULL_UP)        

servo1 = Servo(Pin(15))
servo1.write_angle(45) #45 = เริ่ม (ตั้งฉาก) 150 นอน
time.sleep(2)
#servo1.write_angle(150)
#time.sleep(2)
#servo1.write_angle(45) #45 = เริ่ม (ตั้งฉาก) 150 นอน
#time.sleep(2)