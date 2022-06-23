from machine import Pin,ADC
from neopixel import NeoPixel
import time

pin = Pin(23, Pin.OUT)
np = NeoPixel(pin, 8)

adc = ADC(Pin(36))

while True:
    val = adc.read_u16()
    time.sleep(0.3)
    print(val)
    if val >= 10000:
        np[0] = (25, 0, 0)
        np.write()
    else:
        np[0] = (0, 0, 0)
        np.write()

