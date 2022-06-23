from machine import Pin, PWM
import time

Buzzer_Pin = Pin(32,Pin.OUT) #ออดเป็น Output ที่อยู่บน Pin 32 ของบอร์ด

buzzer = PWM(Buzzer_Pin, freq=1674, duty=1000) # PWMเป็นคำสั่งทำงานและกำหนด PIN ความถี่ ละก็ความดังมั้ง
time.sleep(1)
buzzer = PWM(Buzzer_Pin, freq=627, duty=1000)
time.sleep(1)

buzzer.deinit()