import serial
from mqtt_publisher import MQTT

ser = serial.Serial('/dev/ttyUSB0', 9600) # Lendo os dados da porta serial
comunicacao = MQTT("mqtt-dashboard.com")

def enviar_mensagem(msg):
    print("Enviando NTU: ", msg)
    comunicacao.enviar_mensagem(msg)

while True:
    data = ser.readline().decode('utf-8').strip()
    enviar_mensagem(data)
