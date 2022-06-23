from machine import Pin
from neopixel import NeoPixel
import time
import random

pin = Pin(23, Pin.OUT)
np = NeoPixel(pin, 8) 

colorlist= []

R = 0
G = 0
B = 25
while True:
    if R <= 25 and B >= 0:
        np[0] = (R, G, B)
        R += 1
        B -= 1
        np.write()
        
        time.sleep(0.1)
        print(R,G,B)
    else:
        break