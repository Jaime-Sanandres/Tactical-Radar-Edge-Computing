# Tactical Radar System with Edge Filtering

![Project Status](https://img.shields.io/badge/Status-Completed-success)
![Hardware](https://img.shields.io/badge/Hardware-Arduino_Uno-blue)
![Python](https://img.shields.io/badge/Python-Pygame-yellow)
![C++](https://img.shields.io/badge/C%2B%2B-Edge_Computing-purple)

<img width="200" height="355.5" alt="radar_demo" src="https://github.com/user-attachments/assets/be1a90bb-fe6e-46f3-aba0-e650f7b1c1de" />




An active hardware-software radar scanner that maps its physical surroundings in real-time. This project uses an ultrasonic sensor mounted on a servomotor to sweep the environment, applies an **Edge Computing noise filter in C++** directly on the microcontroller to clean the data, and streams it via serial to a Python-based tactical UI.

## 🧠 Core Features & Engineering Concepts

*   **Edge Data Filtering (Edge AI Precursor):** Cheap ultrasonic sensors capture a lot of noise and "ghost" readings. Instead of sending raw, messy data, the Arduino runs a custom C++ moving average/median filter to discard outliers before transmission, sending only stable data.
*   **Hardware-to-PC Telemetry:** Real-time serial communication sending formatted `Angle,Distance` packets from the microcontroller to the computer.
*   **Polar to Cartesian Trigonometry:** Python translates raw angles and distances (polar coordinates) into X/Y screen coordinates (Cartesian) using `math.sin()` and `math.cos()` to plot targets accurately.
*   **Custom GUI:** A tactical military-style green radar interface built in Python that dynamically draws the sweeping radar arc and red blips where objects are detected.

## 🛠️ Hardware & Tech Stack

**Hardware (BOM):**
*   1x Arduino Uno R3 (or compatible clone)
*   1x HC-SR04 Ultrasonic Sensor
*   1x SG90 Micro Servomotor (Actuator)
*   1x Breadboard (Medium size)
*   Jumper Wires (Male-Male, Male-Female)
*   *Pro-tip: Use a small piece of cardboard/plastic and glue to securely mount the sensor on top of the servo arm.*

**Software:**
*   **C++ (Arduino IDE):** Servo control loops, ultrasonic pulse timing, edge filtering math algorithms, and serial formatting.
*   **Python 3:** `pyserial` for data ingestion, `pygame` (or `matplotlib`) for real-time graphics rendering.

## 🔌 Wiring Guide

| Component | Pin | Arduino Pin | Description |
| :--- | :--- | :--- | :--- |
| **HC-SR04** | VCC | 5V | Power |
| | GND | GND | Ground |
| | TRIG | Digital 9 | Trigger Pulse |
| | ECHO | Digital 10 | Echo Read |
| **SG90 Servo**| Red (VCC) | 5V | Power |
| | Brown (GND) | GND | Ground |
| | Orange (SIG) | Digital 11 | PWM Signal (`Servo.h`) |

## 🚀 How to Run the Project

### 1. Arduino Setup (Hardware & Edge Filter)
1. Assemble the hardware and wire it according to the table above.
2. Open the `arduino_src` folder and upload the `.ino` code to your Arduino.
3. The servo will start sweeping from 0º to 180º. Open the **Serial Monitor** to verify the filtered data stream (Format: `Angle,Distance`).

### 2. Python Setup (Radar UI)
1. Ensure Python 3.x is installed. Install the required dependencies in your terminal:
   ```bash
   pip install pyserial pygame
   ```
2. Open `radar_ui.py` in the `python_ui` folder.
3. Update the COM port line to match your Arduino's connection (e.g., `COM3` for Windows, `/dev/ttyUSB0` for Linux/Mac):
   ```python
   # Initialize serial connection
   arduino_port = serial.Serial('COM3', 115200)
   ```
4. Run the script. Put your hand in front of the physical sensor and watch the red dot appear on the radar screen!

## 🛟 MVP / Troubleshooting Mode (No Python)

If you experience environment issues with Python or the graphical interface, you can still visualize the data perfectly using Arduino's native tools (Minimum Viable Product):

1. Open the Arduino IDE.
2. Instead of the Serial Monitor, open the **Serial Plotter** (`Tools > Serial Plotter`).
3. The Arduino IDE will automatically draw real-time graphs showing the peaks where objects are detected. 
4. *Engineering Highlight:* You can clearly demonstrate the Edge Filter in action here by recording the screen, showing how the graph goes from having false, noisy spikes to being totally stable once the C++ filter is applied!

## 🤝 Connect
Created by Jaime Sanandrés. Check out the demonstration video and a deep dive into the Edge Filtering algorithm on my [LinkedIn Profile](https://www.linkedin.com/in/jaime-sanandr%C3%A9s-aa6b93308/?locale=en-US)!
