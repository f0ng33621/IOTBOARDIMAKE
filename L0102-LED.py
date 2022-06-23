from machine import Pin
from neopixel import NeoPixel
import time

pin = Pin(23, Pin.OUT) # set GPIO23 to output to drive NeoPixels
np = NeoPixel(pin, 8) # create NeoPixel driver on GPIO0 for 8 pixels

while True:
    np[0] = (0, 0, 0)
    np.write()
    time.sleep(1)
    np[0] = (25, 0, 0)
    np.write()
    time.sleep(1)
    np[0] = (0, 0, 0)
    np.write()
    time.sleep(1)
    np[0] = (0, 25, 0)
    np.write()
    time.sleep(1)
    np[0] = (0, 0, 0)
    np.write()
    time.sleep(1)
    np[0] = (0, 0, 25)
    np.write()
    time.sleep(1)