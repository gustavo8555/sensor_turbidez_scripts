import paho.mqtt.client as mqtt

class MQTT:
    # host
    def conectar_client(self, host):
        client = mqtt.Client(client_id="", protocol=mqtt.MQTTv311)
        connection = client.connect(host=host)
        return (client, connection)
    
    def enviar_mensagem(self, msg):
        self.client.publish(topic="casa/sensor_turbidez", payload=msg)
    
    def __init__(self, host):
        print("Criando conexão")
        self.client, self.connection = self.conectar_client(host)

