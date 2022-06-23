from machine import Pin
from neopixel import NeoPixel

pin = Pin(23, Pin.OUT) # set GPIO23 to output to drive NeoPixels
np = NeoPixel(pin, 8) # create NeoPixel driver on GPIO0 for 8 pixels
#         R    G    B
np[0] = (25, 25, 22) # set the first pixel to white
np[1] = (20, 0, 20) # set the second pixel to white

np.write() # write data to all pixels