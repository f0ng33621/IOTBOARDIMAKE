from machine import Pin
import time

Relay1 = Pin(14,Pin.OUT)
Relay2 = Pin(27,Pin.OUT)

while True:
    Relay1.value(0)
    Relay2.value(0)
    time.sleep(0.1)

    Relay1.value(1)
    Relay2.value(1)
    time.sleep(0.1)