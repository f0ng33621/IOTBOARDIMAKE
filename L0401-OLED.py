import ssd1306
from machine import Pin , SoftI2C

i2c = SoftI2C(scl=Pin(22), sda=Pin(21))

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

oled.text('Praweenwat',0,0)
oled.text('Wongsatorn',10,10)
oled.text('Rapeepat',20,20)
oled.show()

#oled.fill(0)
#oled.show()