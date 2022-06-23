from machine import Pin
from neopixel import NeoPixel
import time

pin = Pin(23, Pin.OUT)
np = NeoPixel(pin, 8)

button1 = Pin(15, Pin.IN, Pin.PULL_UP)
button2 = Pin(2, Pin.IN, Pin.PULL_UP)
button3 = Pin(0, Pin.IN, Pin.PULL_UP)
button4 = Pin(4, Pin.IN, Pin.PULL_UP)

Relay1 = Pin(14,Pin.OUT)
Relay2 = Pin(27,Pin.OUT)

while True:
    Btn1_state = button1.value()
    Btn2_state = button2.value()
    Btn3_state = button3.value()
    Btn4_state = button4.value()
    time.sleep(0.5)
    if Btn1_state == 0:
        np[0] = (25, 0, 0)
        np.write()
        Relay1.value(0)
        time.sleep(0.1)
        Relay1.value(1)
        time.sleep(0.1)
    elif Btn2_state == 0:
        np[1] = (25, 0, 0)
        np.write()
        Relay2.value(0)
        time.sleep(0.1)
        Relay2.value(1)
        time.sleep(0.1)
    elif Btn3_state == 0:
        np[0] = (0, 0, 0)
        np.write()
        Relay1.value(0)
        time.sleep(0.1)
    elif Btn4_state == 0:
        np[1] = (0, 0, 0)
        np.write()
        Relay2.value(0)
        time.sleep(0.1)
