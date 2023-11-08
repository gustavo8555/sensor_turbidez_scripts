import serial

ser = serial.Serial('/dev/ttyUSB0', 9600) # Lendo os dados da porta serial

def enviar_mensagem(msg):
    print("Enviando NTU: ", msg)
    pass

while True:
    data = ser.readline().decode('utf-8').strip()
    enviar_mensagem(data)
