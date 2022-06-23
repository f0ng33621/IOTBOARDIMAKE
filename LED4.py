from machine import Pin
from neopixel import NeoPixel
import time
import random

pin = Pin(23, Pin.OUT)
np = NeoPixel(pin, 8) 


colorlist= []


while True:
    R = random.randint(0,25)
    G = random.randint(0,25)
    B = random.randint(0,25)
    if R <= 25 and B >= 0:
        np[0] = (R, G, B)
        np.write()
        
        time.sleep(0.5)
        print(R,G,B)
    else:
        break
    
#for i in range (0,255,1):
    #if R <= 255 and B >= 0:
        #np[0] = (i,)