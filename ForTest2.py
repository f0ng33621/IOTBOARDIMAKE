import network #! Library ที่ Import มาต้องไปลองใน Thonny อีกรอบ
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


Ultra1 = HCSR04(33, 25) #รถไฟ
Ultra2 = HCSR04(18, 19) #Yellow line
Ultra3 = HCSR04(17, 16) #ร่วง
Buzzer_Pin = Pin(32,Pin.OUT)
button4 = Pin(4, Pin.IN, Pin.PULL_UP)
servo1 = Servo(Pin(15))
adc = ADC(Pin(36))
#servo1.write_angle(45)

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


while True:
    
    resultMo1 = Ultra1.distance_cm() #รถไฟ
    print("SS1",resultMo1)
    time.sleep(0.5)
    resultMo2 = Ultra2.distance_cm() #Yellow line
    print("SS2",resultMo2)    
    time.sleep(0.5)
    resultMo3 = Ultra3.distance_cm() #ร่วง
    print("SS3",resultMo3)    
    time.sleep(0.5)
    Btn4_state = button4.value()
    time.sleep(0.25)
    print("Button4",Btn4_state)
    val = adc.read_u16()
    print(val)

    if resultMo2 < 7: #เดินใกล้
        
        buzzer = PWM(Buzzer_Pin, freq=1674, duty=5000)
        time.sleep(0.1)
        buzzer = PWM(Buzzer_Pin, freq=627, duty=5000)
        time.sleep(0.05)
        buzzer = PWM(Buzzer_Pin, freq=1674, duty=5000)
        time.sleep(0.1)
        buzzer = PWM(Buzzer_Pin, freq=627, duty=5000)
        time.sleep(0.05)
        client.publish('@shadow/data/update',
            json.dumps({
                'data' : {
                    'YellowLine': "Detected"
                }
            }))
    elif resultMo2 >= 7:
        buzzer = PWM(Buzzer_Pin, freq=0, duty=0)
        time.sleep(0.1)
        client.publish('@shadow/data/update',
            json.dumps({
                'data' : {
                    'YellowLine': "Normal"
                }
            }))
            time.sleep(0.01)