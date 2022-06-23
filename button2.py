#importlibrary
from machine import Pin
from neopixel import NeoPixel
import time

#setup pin
button1 = Pin(15, Pin.IN, Pin.PULL_UP) #ปุ่มที่ 1 อยู่บน Pin 15 ของบอร์ดและต้องกำหนดให้เป็น Input
button2 = Pin(2, Pin.IN, Pin.PULL_UP)
button3 = Pin(0, Pin.IN, Pin.PULL_UP)
button4 = Pin(4, Pin.IN, Pin.PULL_UP)

pin = Pin(23, Pin.OUT)
np = NeoPixel(pin, 8) #LED บนบอร์ดเป็น Output

while True:
    Btn1_state = button1.value()
    Btn2_state = button2.value()
    Btn3_state = button3.value()
    Btn4_state = button4.value()
    time.sleep(0.5)
    if Btn1_state == 0: #ถ้ากดให้ไฟติด
        np[0] = (25, 0, 0)
        np.write()
    elif Btn2_state == 0:
        np[1] = (25, 0, 0)
        np.write()
    elif Btn3_state == 0:
        np[0] = (0, 0, 0)
        np.write()
    elif Btn4_state == 0:
        np[1] = (0, 0, 0)
        np.write()
    