import serial
import time
import math

# 1. Establish serial connection (adjust your 'COM3' port if necessary)
arduino_port = serial.Serial('COM3', 9600)
time.sleep(2)

print("Starting polar to Cartesian coordinate conversion...")

while True:
    if arduino_port.in_waiting > 0:
        # Read the line from Arduino
        line = arduino_port.readline().decode('utf-8').strip()
        
        # Try to process the data (prevent the program from crashing if an empty line arrives)
        try:
            # Split the string by the comma programmed in C++
            parts = line.split(',')
            if len(parts) == 2:
                angle_degrees = float(parts[0])
                distance = float(parts[1])
                
                # MATHEMATICAL CONVERSION
                # 1. Convert degrees to radians for Python
                angle_radians = math.radians(angle_degrees)
                
                # 2. Calculate X and Y coordinates using trigonometry
                # (Multiply the distance by a scale factor if the numbers are too large for pixels)
                x = distance * math.cos(angle_radians)
                y = distance * math.sin(angle_radians)
                
                # Print the result to the console for validation
                print(f"Angle: {angle_degrees}° | Dist: {distance} cm ---> X: {x:.2f}, Y: {y:.2f}")
                
        except ValueError:
            # If the cable sends a corrupted or incomplete packet, ignore it without breaking the loop
            pass
