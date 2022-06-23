from machine import Pin,ADC
import time

adc = ADC(Pin(36))        # create an ADC object acting on a pin

while True:
    val = adc.read_u16()  # read a raw analog value in the range 0-65535
    print(val)
    time.sleep(0.3)
