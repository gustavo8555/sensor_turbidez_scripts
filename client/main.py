import paho.mqtt.client as mqtt
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def update(frame):
    line.set_data(range(len(data)), data)
    return line,

def generates_graph(update):
    return FuncAnimation(fig, update, blit=True, interval=100)

def save_list_to_file(file_path, data_list):
    """
    Saves the result to a text file.

    Parameters:
    - file_path (str): The path to the text file.
    - data_list (list): The list to save.
    """
    print("----- SAVING RESULTS FILE -----")
    with open(file_path, 'w') as file:
        for item in data_list:
            file.write(str(item) + '\n')

def message_receiver(client, userdata, message):
    NTU = float(message.payload.decode("utf-8"))
    data.append(NTU)
    print(NTU)
    if len(data) == expected_file_size:
        save_list_to_file(file_path, data) # creates a file with the results
    if len(data) > 100:
        data.pop(0)  # Remove the oldest data point if the list is too long
    print("Received measurement...")

## Sensor File settings
expected_file_size = 60
file_was_created = True
file_path = 'sensor_data.txt'

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