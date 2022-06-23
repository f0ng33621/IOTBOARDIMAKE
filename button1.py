#importlibrary
from machine import Pin
import time

#setup pin
button1 = Pin(15, Pin.IN, Pin.PULL_UP)
button2 = Pin(2, Pin.IN, Pin.PULL_UP)
button3 = Pin(0, Pin.IN, Pin.PULL_UP)
button4 = Pin(4, Pin.IN, Pin.PULL_UP)

while True:
    Btn1_state = button1.value()  #Value = 0,1
    Btn2_state = button2.value()
    Btn3_state = button3.value()
    Btn4_state = button4.value()
    print(Btn1_state, Btn2_state, Btn3_state, Btn4_state)
    time.sleep(0.5)