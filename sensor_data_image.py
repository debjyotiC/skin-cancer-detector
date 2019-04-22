import serial
import matplotlib.pyplot as plt
import numpy as np

arduino_port = 'COM17'
arduino_baud = 9600

ser = serial.Serial(arduino_port, arduino_baud, timeout=3.0)
data_got = []
pos = []

for itr in range(17):
    # sleep(2)
    ser.write(str.encode('C'))
    data_read = ser.readline()
    pos.append(itr)
    if itr >= 1:
        data_got.append(round(int(data_read.decode('ascii').replace("\r\n", ""))*(5/1023), 4))

new_data = np.resize(np.array(data_got), (4, 4))
print(new_data)
plt.imshow(new_data, cmap='hot', interpolation='nearest')
plt.show()
