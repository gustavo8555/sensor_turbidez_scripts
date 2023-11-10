import paho.mqtt.client as mqtt
import time

def message_receiver(client, userdata, message):
    time.sleep(1)
    print("Chegou mensagem...")
    print(str(message.payload.decode("utf-8")))

client = mqtt.Client(client_id="pi", protocol=mqtt.MQTTv311)
conection = client.connect(host="192.168.15.82")

client.loop_start()
client.subscribe("casa/sensor_turbidez")

while True:
    client.on_message=message_receiver