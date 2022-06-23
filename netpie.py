import network #import Network สำหรับเชื่อมข้อมูลขึ้น Server
from machine import Pin #import machine ให้สามารถใช้อุปกรณ์บนบอร์ดได้
from simple import MQTTClient #MQTT เป็นตัว Service
from neopixel import NeoPixel #แสงไฟบนบอร์ด
import dht #จำไม่ได้
import json #ใช้ส่งlog ขึ้น Server
import machine 
import time 


d = dht.DHT11(machine.Pin(13))

button1 = Pin(15, Pin.IN, Pin.PULL_UP) #Button มีอยู่่ที่ตัวบอร์ดอยู่แล้ว มี 4 ปุ่ม (FIX Pinอยู่แล้ว)
button2 = Pin(2, Pin.IN, Pin.PULL_UP)  #Button มีอยู่่ที่ตัวบอร์ดอยู่แล้ว มี 4 ปุ่ม (FIX Pinอยู่แล้ว)
button3 = Pin(0, Pin.IN, Pin.PULL_UP) #Button มีอยู่่ที่ตัวบอร์ดอยู่แล้ว มี 4 ปุ่ม (FIX Pinอยู่แล้ว)
button4 = Pin(4, Pin.IN, Pin.PULL_UP) #Button มีอยู่่ที่ตัวบอร์ดอยู่แล้ว มี 4 ปุ่ม (FIX Pinอยู่แล้ว)

Relay1 = Pin(14,Pin.OUT) #Relay มีกับบอร์ด 2 ตัว (FIX Pinอยู่แล้ว)
Relay2 = Pin(27,Pin.OUT) #Relay มีกับบอร์ด 2 ตัว (FIX Pinอยู่แล้ว)

pin = Pin(23, Pin.OUT) #ลืม!!!
np = NeoPixel(pin, 8) #ถ้าจำไม่ผิดจะเป็น RGB led บนบอร์ด

wlan = network.WLAN(network.STA_IF) #ต่อเน็ต
wlan.active(True)
print('Wifi Connecting...')
wlan.connect('iMakeEDU','imake1234') #กำหนด ขื่อ รหัสผ่าน
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

while True: #วัดค่าต่างๆ
    d.measure()
    temp = d.temperature()
    hum = d.humidity()
    Btn1_state = button1.value()
    Btn2_state = button2.value()
    Btn3_state = button3.value()
    Btn4_state = button4.value()
    
    Relay1.value(0) #ถ้าค่าRelay == 0 ให้ส่งไปหาServerด้วย json dump ชื่อสถานะไปว่า OFF ในตัวแปร Relay1
    client.publish('@shadow/data/update',
                json.dumps({
                    'data' : {
                        'Relay1' : 'OFF'
                       }
                    }))
    
    if Btn1_state == 0: #ถ้ากดปุ่ม
        np[0] = (20,0,0) #ไฟดวงแรกขึ้นสีนี้
        np.write() #คำสั่งทำงาน
        time.sleep(0.5) #พักแปป
        np[0] = (0,0,0) #ปิดไฟ
        np.write() #คำสั่งทำงาน
        Relay1.value(1) #Relay ทำงานด้วย
        print(Relay1) #ตรวจสอบค่าเฉยๆ
        client.publish('@shadow/data/update', #Update Status Monitoring
                   json.dumps({
                       'data' : {
                           'Relay1' : 'ON'
                           }
                        }))
        
    print('Temperature:',temp,'Humidity:',hum) 
    client.publish('@shadow/data/update',
                   json.dumps({
                       'data' : {
                           'temperature' : temp,
                           'Humidity' : hum,
                           }
                       
                       }))
    time.sleep(0.5)
