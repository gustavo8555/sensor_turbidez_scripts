import paho.mqtt.client as mqtt
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time

def update(frame):
    line.set_data(range(len(data)), data)
    return line,

def generates_graph(update):
    return FuncAnimation(fig, update, blit=True, interval=100)

def message_receiver(client, userdata, message):
    NTU = float(message.payload.decode("utf-8"))
    data.append(NTU)
    print(NTU)
    if len(data) > 100:
        data.pop(0)  # Remove the oldest data point if the list is too long
    print("Received measurement...")

data = []

fig, ax = plt.subplots()
line, = ax.plot([], [])

# Set the axis limits
ax.set_xlim(0, 100)
ax.set_ylim(1000, 5000)

client = mqtt.Client(client_id="pi", protocol=mqtt.MQTTv311)

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("casa/sensor_turbidez")

client.on_connect = on_connect
client.on_message = message_receiver

conection = client.connect(host="192.168.15.82")
client.loop_start()

ani = generates_graph(update)

plt.show()