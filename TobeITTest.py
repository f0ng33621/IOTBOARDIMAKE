from machine import Pin, I2C, PWM
import ssd1306
from hcsr04 import HCSR04
from time import sleep
from neopixel import NeoPixel
import time
import network 
import socket 
from simple import MQTTClient
import dht
import json
from machine import *


pin = Pin(23, Pin.OUT)
np = NeoPixel(pin, 8)
d = dht.DHT11(Pin(13))
Relay1 = Pin(14,Pin.OUT)
Relay2 = Pin(27,Pin.OUT)

i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
sensor = HCSR04(trigger_pin=5, echo_pin=18, echo_timeout_us=10000)


wlan = network.WLAN(network.STA_IF) #ต่อเน็ต
wlan.active(True)
print('Wifi Connecting...')
wlan.connect('AndroidAP10be','pqac8403') #กำหนด ขื่อ รหัสผ่าน
while not wlan.isconnected():
    pass # pass this loop until wlan.isconnected is True

print('Wifi Connected!')
print(wlan.ifconfig())


MQTT_Client_ID = '36c68204-b8a2-40f4-a7a6-701dfc3cdbb6' #ได้จาก Service ที่เราconnect ไปแล้วเขาจะให้มา
MQTT_Token = 'AYtsQWSJhpDGAkY2GFpZJKuWhbSfYhRr'
MQTT_Secret = '2_87Xr5cxUF2BOXedviHQmEo0L0fg57m'
MQTT_Broker = 'mqtt.netpie.io'
# Create Netpie profile
client = MQTTClient(MQTT_Client_ID, MQTT_Broker,user=MQTT_Token, password=MQTT_Secret)

# connect to netpie
client.connect()

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)


while True:
  d.measure()
  temp = d.temperature()
  hum = d.humidity()
  oled.fill(0)
  distance = sensor.distance_cm()
  print('Distance:', distance, 'cm')
  oled.text("Distance (cm)", 0, 15)
  oled.text(str(distance), 0, 35)
  oled.show()
  sleep(1) #ถ้าค่าRelay == 0 ให้ส่งไปหาServerด้วย json dump ชื่อสถานะไปว่า OFF ในตัวแปร Relay
  if distance <= 6 :
    np[0] = (25, 0, 0)
    np.write()
    Relay1.value(1)
    time.sleep(0.5)

  elif distance >6 :
    np[0] = (0,0,0)
    np.write()
    Relay1.value(0)
    time.sleep(0.5)
    #client.publish(@shadow/data/update)
    
    
