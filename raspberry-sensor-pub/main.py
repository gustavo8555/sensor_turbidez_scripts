import sys
import serial
from mqtt_publisher import MQTT

ser = serial.Serial('/dev/ttyUSB0', 9600) # Lendo os dados da porta serial
# TODO: add an error message if the not informs the MQTT address server
broker = sys.argv[1]
comunicacao = MQTT(broker)

def enviar_mensagem(msg):
    print("Enviando NTU: ", msg)
    comunicacao.enviar_mensagem(msg)

while True:
    data = ser.readline().decode('utf-8').strip()
    enviar_mensagem(data)
