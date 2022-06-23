
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
#from tkinter import * 
#import tkinter


wlan = network.WLAN(network.STA_IF)
wlan.active(True)
print('Wifi Connecting...')
wlan.connect('iMakeEDU','imake1234')
while not wlan.isconnected():
    pass 


print('Wifi Connected!')
print(wlan.ifconfig())


MQTT_Client_ID = '36c68204-b8a2-40f4-a7a6-701dfc3cdbb6'
MQTT_Token = 'AYtsQWSJhpDGAkY2GFpZJKuWhbSfYhRr'
MQTT_Secret = '2_87Xr5cxUF2BOXedviHQmEo0L0fg57m'
MQTT_Broker = 'mqtt.netpie.io'

client = MQTTClient(MQTT_Client_ID, MQTT_Broker,user=MQTT_Token, password=MQTT_Secret)

client.connect()
client.publish('@shadow/data/update',
                json.dumps({
                    'data' : {
                        'Stair': "CLOSE"
                    }
                }))
