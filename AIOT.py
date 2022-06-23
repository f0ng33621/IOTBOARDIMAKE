import network #! Library ที่ Import มาต้องไปลองใน Thonny อีกรอบ
import socket # ให้ TEN อธิบายน่าจะได้555555
from simple import MQTTClient
from neopixel import NeoPixel #ใช้ LED
import dht 
import json
import machine
import time
from machine import Pin, PWM
from machine import *
from hcsr04 import HCSR04 #HCSR04 เป็นเซนเซอร์ที่ซื้อมาแล้วทำการโหลด module มาใช้จากเน็ตเราก็ import เข้ามาใช้



Ultra1 = HCSR04(33, 25) #HCSR Sensor 1
Ultra2 = HCSR04(18, 19) #HCSR Sensor 2
Ultra3 = HCSR04(17, 16) #HCSR Sensor 3
Buzzer_Pin = Pin(32,Pin.OUT) #BUZZER FIX
button1 = Pin(15, Pin.IN, Pin.PULL_UP) #BUTTON FIX
button2 = Pin(2, Pin.IN, Pin.PULL_UP) #BUTTON FIX
button3 = Pin(0, Pin.IN, Pin.PULL_UP) #BUTTON FIX
button4 = Pin(4, Pin.IN, Pin.PULL_UP) #BUTTON FIX


wlan = network.WLAN(network.STA_IF) #Connect Internet
wlan.active(True)
print('Wifi Connecting...')
wlan.connect('iMakeEDU','imake1234') # WIFINAME , PASSWORD
while not wlan.isconnected():
    pass 

print('Wifi Connected!')
print(wlan.ifconfig())


MQTT_Client_ID = '36c68204-b8a2-40f4-a7a6-701dfc3cdbb6' #USE MQTT SERVICE
MQTT_Token = 'AYtsQWSJhpDGAkY2GFpZJKuWhbSfYhRr'
MQTT_Secret = '2_87Xr5cxUF2BOXedviHQmEo0L0fg57m'
MQTT_Broker = 'mqtt.netpie.io'

client = MQTTClient(MQTT_Client_ID, MQTT_Broker,user=MQTT_Token, password=MQTT_Secret)

client.connect()


while True:

    resultMo1 = Ultra1.distance_cm() #CHECK ค่าของ Sensor ตัวที่ 1 
    print("SS1",resultMo1)
    time.sleep(0.5)
    resultMo2 = Ultra2.distance_cm() #Yellow line #CHECK ค่าของ Sensor ตัวที่ 2 
    print("SS2",resultMo2)     
    time.sleep(0.5)
    resultMo3 = Ultra3.distance_cm() #ร่วง #CHECK ค่าของ Sensor ตัวที่ 3 
    print("SS3",resultMo3)    
    time.sleep(0.5)
    Btn1_state = button1.value() #กำหนดให้ Btn_State เก็บค่าของ ปุ่ม
    Btn2_state = button2.value()
    Btn3_state = button3.value()
    Btn4_state = button4.value()
    
    if resultMo2 < 250: #เดินใกล้
        
        buzzer = PWM(Buzzer_Pin, freq=1674, duty=5000) #Buzzer ทำงาน
        time.sleep(0.1) #พักแป๊ป
        buzzer = PWM(Buzzer_Pin, freq=627, duty=5000)
        time.sleep(0.1) #คิดจะพัก
        buzzer = PWM(Buzzer_Pin, freq=1674, duty=5000)
        time.sleep(0.1) #คิดถึงคิตแคต
        buzzer = PWM(Buzzer_Pin, freq=627, duty=5000)
        time.sleep(0.1)
        client.publish('@shadow/data/update', # Push ค่าขึ้นให้ดูผ่าน Monitoring
            json.dumps({
                'data' : {
                    'YellowLine': "Detected"
                }
            }))
    elif resultMo2 >= 250: #น้อยกว่าค่า 250 ให้มีเสียงออด
        buzzer = PWM(Buzzer_Pin, freq=1674, duty=0)
        time.sleep(0.1)
        client.publish('@shadow/data/update',
            json.dumps({
                'data' : {
                    'YellowLine': "Normal"
                }
            }))    