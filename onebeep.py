import dht
import machine
import time

d = dht.DHT11(machine.Pin(13))

while True:
    d.measure()
    temp = d.temperature() # eg. 23 (°C)
    hum = d.humidity()    # eg. 41 (% RH)
    print('Temperature:',temp,'Humidity:',hum)
    time.sleep(0.1)