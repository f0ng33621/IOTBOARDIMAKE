import network

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
print('Wifi Connecting...')
wlan.connect('iMakeEDU','imake1234')
while not wlan.isconnected():
    pass # pass this loop until wlan.isconnected is True

print('Wifi Connected!')
print(wlan.ifconfig())