import paho.mqtt.client as mqtt

client = mqtt.Client(client_id="", protocol=mqtt.MQTTv311)
conection = client.connect(host="mqtt-dashboard.com")

client.publish(topic="casa/sensor_turbidez", payload="ligado")

print("Mensagem enviada")
