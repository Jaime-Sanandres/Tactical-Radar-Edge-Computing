# Tactical Radar System with Edge-Computed Signal Filtering 📡

A hardware-software integrated tactical radar system featuring edge-computed signal filtering in C++ and a real-time Python visual telemetry interface converting polar coordinates into Cartesian coordinates.

## Overview

This project bridges the gap between physical hardware and digital signal processing. Built as a foundation for understanding embedded systems in the aerospace and defense sectors, it scans its surroundings using ultrasonic sensing, filters measurement noise and spurious reflections at the microcontroller level (Edge Computing), and streams clean telemetry to a Python-based tactical UI.

## Hardware Architecture

The physical layer is built using accessible, off-the-shelf components, forcing the software to handle the complexities of mechanical timing and sensor noise:
* **Microcontroller:** Arduino Uno R3
* **Sensor:** HC-SR04 Ultrasonic Module
* **Actuator:** SG90 Micro Servo Motor
* **Prototyping:** Standard Breadboard and Jumper Wires

## The Technical Core: Edge Computing (C++)

Cheap ultrasonic sensors inherently pick up measurement outliers caused by acoustic reflections and sensor uncertainty, which translates into "ghosts" on the radar screen. Instead of relying on the PC to clean the data, this system implements an **Edge Computing** approach directly on the Arduino using C++:
* **Median Filter Algorithm:** For each angular position, the system performs three consecutive ultrasonic measurements.
* **Crosstalk Mitigation:** A controlled delay between consecutive measurements allows acoustic echoes to decay before the next pulse is triggered.
* **On-Board Processing:** The C++ program sorts the three readings mathematically and selects the median value, rejecting isolated measurement outliers before formatting and transmitting the telemetry via the Serial port.

## Real-Time Telemetry & Visualization (Python)

The clean telemetry stream (`Angle,Distance`) is read via USB using `pyserial`. The visual interface is built with `pygame`:
* **Mathematical Mapping:** Converts polar coordinates from the hardware into Cartesian coordinates (X, Y) using `math.cos()` and `math.sin()`.
* **Dynamic Range Optimization:** The UI scale is heavily optimized for short-range detection (20 cm), ensuring maximum visual sensitivity and real-time tracking of small changes in measured distance.
* **Motion Blur Effect:** Implements a fading alpha channel to simulate the radar-style trail.

## Repository Structure

The files are sequentially numbered to reflect the engineering process, from physical testing to software integration:

* **Hardware & C++ (Arduino)**
  * `01_servo_sweep_test.ino` - Initial mechanical calibration.
  * `02_ultrasonic_sensor_test.ino` - Sensor timing and math.
  * `03_hardware_integration_raw.ino` - First hardware integration (raw data).
  * `07_edge_computing_median_filter.ino` - **Final C++ Core with Edge Filter.**

* **Software & Python (PC)**
  * `04_serial_telemetry_test.py` - Establishing the serial link.
  * `05_polar_to_cartesian_math.py` - Trigonometric conversions.
  * `06_tactical_radar_ui.py` - **Final Pygame UI with short-range optimized scaling.**

## How to Run

1. **Wiring:**
   * Servo signal to Pin 9.
   * Sensor `Trig` to Pin 10.
   * Sensor `Echo` to Pin 11.
2. **Flash the Microcontroller:** Upload `07_edge_computing_median_filter.ino` to the Arduino. Make sure to close the Serial Monitor afterwards to free the USB port.
3. **Environment Setup:** Ensure Python is installed on your PC, then install the required libraries via terminal:
   
```bash
pip install pyserial pygame
```

4. **Launch the Radar:**
   
```bash
python 06_tactical_radar_ui.py
```
