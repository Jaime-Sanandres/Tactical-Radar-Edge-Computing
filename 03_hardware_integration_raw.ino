#include <Servo.h>

// 1. HEADER & SETUP
// Servo object definition
Servo miMotor;

// Define the pins for the ultrasonic sensor
const int trigPin = 10;
const int echoPin = 11;

// Variables to store the time duration and the calculated distance
long duration;
long distance;

void setup() {
  // Initialize servo on pin 9
  miMotor.attach(9);
  
  // Configure sensor pins
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  
  // Initialize the Serial Monitor at 9600 baud rate
  Serial.begin(9600);
}

// 2. THE CHOREOGRAPHY
void loop() {
  int i;
  
  // First loop: sweep from 0 to 180 degrees
  for(i = 0; i <= 180; i++) {
    // Tell the motor to go to the current degree
    miMotor.write(i);
    
    // Clear the Trig pin first to ensure a clean pulse
    digitalWrite(trigPin, LOW);
    delayMicroseconds(2);
    
    // Send a 10-microsecond HIGH pulse to trigger the sensor
    digitalWrite(trigPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW);
    
    // Wait for the echo and get the time in microseconds
    duration = pulseIn(echoPin, HIGH);
    
    // Calculate the distance mathematically
    distance = duration * 0.034 / 2;
    
    // 3. DATA FORMATTING
    // Send the formatted data strictly as "Angle,Distance" for Python
    Serial.print(i);
    Serial.print(",");
    Serial.println(distance);
    
    // 4. TIMING ADJUSTMENT
    // Give time for the motor to move and sound waves to dissipate
    delay(30);
  }
  
  // Second loop: sweep from 180 to 0 degrees (return)
  for(i = 180; i >= 0; i--) {
    // Tell the motor to go to the current degree
    miMotor.write(i);
    
    // Clear the Trig pin first to ensure a clean pulse
    digitalWrite(trigPin, LOW);
    delayMicroseconds(2);
    
    // Send a 10-microsecond HIGH pulse to trigger the sensor
    digitalWrite(trigPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW);
    
    // Wait for the echo and get the time in microseconds
    duration = pulseIn(echoPin, HIGH);
    
    // Calculate the distance mathematically
    distance = duration * 0.034 / 2;
    
    // 3. DATA FORMATTING
    // Send the formatted data strictly as "Angle,Distance" for Python
    Serial.print(i);
    Serial.print(",");
    Serial.println(distance);
    
    // 4. TIMING ADJUSTMENT
    // Give time for the motor to move and sound waves to dissipate
    delay(30);
  }
}