import network
from simple import MQTTClient

# Network Interface Mode = station
wlan = network.WLAN(network.STA_IF)
wlan.active(True) # Activate station mode
print('WiFi Connecting...')
wlan.connect('iMakeEDU','imake1234')
while not wlan.isconnected(): # if wlan.isconnected is False
    pass # pass this Loop until wlan.isconnected is True

print('WiFi Connected')
print(wlan.ifconfig())

# Netpie Credential
MQTT_Client_ID = '1e0096ad-377d-45ce-9432-9b86664dcaf1'
MQTT_Token = 'EdCJxMPcpMQu6mG6cbh8upupPennkaGh'
MQTT_Secret = 'sXCEa#SGD~3tZr1#f93NKKOsSTV1R3f7'
MQTT_Broker = 'mqtt.netpie.io'
# Create Netpie Profile
client = MQTTClient(MQTT_Client_ID, MQTT_Broker, user=MQTT_Token, password=MQTT_Secret)

# Connect to Netpie
client.connect()