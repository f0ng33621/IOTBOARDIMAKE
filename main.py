
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
from tkinter import * 
import tkinter


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

Buzzer_Pin = Pin(32,Pin.OUT) 
Motion1 = Pin(,Pin.IN) #* ตั้งก่อนเส้นเหลือง
Motion2 = Pin(,Pin.IN) #* ตั้งเหลื่อมชานชาลาไประยะนึง
Motor1 = Pin(,Pin.OUT) #TODO มาใส่ pin (เป็น pin ของ มอเตอร์ที่ทำให้บันไดทำงาน)
DistanceSensor = Pin(,Pin.IN) #* Sensor ตรวจว่ามีรถไฟมามั้ย
button1 = Pin(15, Pin.IN, Pin.PULL_UP)
button2 = Pin(2, Pin.IN, Pin.PULL_UP)
button3 = Pin(0, Pin.IN, Pin.PULL_UP)
button4 = Pin(4, Pin.IN, Pin.PULL_UP)



while True :#* สำหรับ loop Program
    Btn1_state = button1.value()
    Btn2_state = button2.value()
    Btn3_state = button3.value()
    Btn4_state = button4.value()
# todo 1.1 ใช้ sensor ตรวจว่ามีคนที่กำลังจะเดินเข้าไปในเขตเส้นเหลืองหรือเปล่า
#* def นี้ได้มาจาก https://randomnerdtutorials.com/micropython-interrupts-esp32-esp8266/
    def YellowLine(pin): #? มาใส่เลข port Motion sensor ไม่ทราบว่าเกี่ยวกับ adc มั้ย
        while True :
            pir = Pin(14, Pin.OUT)
            resultMo = pir.irq(trigger=Pin.IRQ_RISING, handler=handle_interrupt) #ใช้ได้อีกตัว>> Pin.IRQ_FALLING: to trigger the interrupt whenever the pin goes from HIGH to LOW;
            print(resultMo) #check result ที่ได้

            if resultMo == '': # todo ผลอยู่ใน resultMo น่าจะมีค่าเป็น 1 เมื่อมีการบัง Sensor
                buzzer = PWM(Buzzer_Pin, freq=1674, duty=1000)
                time.sleep(0.1)
                buzzer = PWM(Buzzer_Pin, freq=1674, duty=1000)
                time.sleep(0.1)
            elif resultMo == '':
                buzzer.deinit()



#// todo 2 ถ้ามีคนตกลงไปข้างล่าง <<< ไปใช้ open cv ดึงรูปจาก iriun webcam 
#!// เช็คด้วยว่าถ้า update main.py ไปลงบอร์ด แล้วมันจะยังจับกล้องได้อยู่หรือเปล่า 
#*// คำแนะนำจากอาจารย์มะ จะต้องมี 3 ส่วน 1.บอร์ดปล่อยให้รันออนไลน์ไปใช้ในการเช็คคนที่จะเข้าเส้นเหลือง 2.Link Webcam เข้าopencvในคอม 3.ส่งต่อไปที่บอร์ด
#!// ลบทิ้งถ้าหากว่าทำไม่ได้หรือไม่ทัน



# todo 3 แจ้งเหตุไปยัง รปภ โดยใช้ gui ที่ควบคุมบอร์ดตัวนี้อยู่ (แบบ Local Computer)
# if opencv or sensor == "": #มาเลือกได้ว่าจะใช้ sensor หรือ opencv ในการเริ่มขั้นตอนนี้
    
#     def CloseStair(): #* รปภ สั่งเก็บบันไดผ่าน gui จากคอมในสถานี
#         Label_Test.config(text = "บันไดกำลังถูกพับเก็บเข้าตำแหน่ง")
#         Label_Test3 = Label(text='ขอย้ำบันไดกำลังถูกพับเก็บเข้าตำแหน่ง',width=40)
#         Label_Test3.pack()
#         Motor1.value(0) #! สั่งให้เก็บบันได Note ไปเช็คว่า Motor นั้นใช้คำสั่งอะไร
#         print(Motor1)
    
#     app = Tk()
#     app.option_add('*font',"Times", "90")
#     app.title("WARNING")
#     app.geometry("500x500")
#     frame = Frame(app)
#     frame.config(background="Grey")
#     frame.place(width=500,height=500,x=0,y=0)
#     Label_Test = Label(text='มีคนตกลงไปจากชานชาลา')
#     Label_Test.config(bg="red")
#     Label_Test.pack()
#     Button_Test = Button(text='ช่วยเหลือแล้ว',command=CloseStair)
#     Button_Test.pack()
#     Label_Test2 = Label(text='อย่ากดปุ่ม ช่วยเหลือแล้ว จนกว่าการช่วยเหลือจะเสร็จสิ้น',width=50,bg='yellow')
#     Label_Test2.pack()
#     app.mainloop() 

# todo 3 เปลี่ยนไปกดปุ่มที่ Board เพื่อหยุดการทำงาน
    if Btn1_state == 0: #เมื่อมีการกดปุ่มให้เก็บบันได
        Motor1.value(0)
        np[0] = (25, 0, 0)
        np.write()
        np[1] = (25, 0, 0)
        np.write()
        np[0] = (0, 0, 0)
        np.write()
        np[1] = (0, 0, 0)
        np.write()        



# todo 4 เก็บบันไดถ้ามีขบวนรถเข้ามาในระยะ
    elif DistanceSensor == : #ถ้ามีรถเข้ามาให้เก็บบันได
        Motor1.value(0) 
        client.publish('@shadow/data/update',
                    json.dumps({
                        'data' : {
                            'Stair': "CLOSE"
                        }
                    }))


# todo 5 ส่ง ข้อมูลเข้าไปบนเว็บ (MQTT) ส่งไปที่ ห้องศูนย์ควบการเดินรถเพื่อที่จะสามารถปรับเปลี่ยนตารางเดินรถให้กระทบผู้โดยสารน้อยที่สุด

    if Motor1 == 1: #ค่า 1 น่าจะเป็นการสั่งทำงาน
        client.publish('@shadow/data/update',
                    json.dumps({
                        'data' : {
                            'Stair': "OPEN"
                        }
                    }))
    elif Motor1 == 0: 
        client.publish('@shadow/data/update',
                    json.dumps({
                        'data' : {
                            'Stair': "CLOSE"
                        }
                    }))
# TODO ไปจัดการสร้างหน้าแสดงผลในเว็บด้วย
