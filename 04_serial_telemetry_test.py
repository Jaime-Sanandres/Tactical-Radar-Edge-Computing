import serial
import time

# 1. ESTABLISH THE CONNECTION
# Change 'COM3' to the exact port used in the Arduino IDE.
# 9600 is the baud rate (must match the C++ code exactly).
arduino_port = serial.Serial('COM3', 9600)
time.sleep(2) # 2-second pause to let the connection stabilize

print("Connection established. Listening to the radar...")

# 2. INFINITE READING LOOP
while True:
    if arduino_port.in_waiting > 0: # If data is waiting on the USB serial buffer
        
        # Read the line, decode it to text, and strip whitespace/newlines
        data_string = arduino_port.readline().decode('utf-8').strip()
        
        # Print the received data to the PC console
        print(data_string)
