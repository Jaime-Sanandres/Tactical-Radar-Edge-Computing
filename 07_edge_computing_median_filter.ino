#include <Servo.h>

// 1. HEADER & SETUP
// Servo object definition
Servo miMotor;

// Define the pins for the ultrasonic sensor
const int trigPin = 10;
const int echoPin = 11;

// Function to get a single raw distance reading
// This prevents repeating the pulse code 6 times in the loop
long getRawDistance() {
  // Clear the Trig pin first to ensure a clean pulse
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  
  // Send a 10-microsecond HIGH pulse to trigger the sensor
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  
  // Wait for the echo and get the time in microseconds
  long duration = pulseIn(echoPin, HIGH);
  
  // Calculate and return the distance mathematically
  return duration * 0.034 / 2;
}

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
    
    // Step 1 & 2: Launch 3 ultra-fast pulses and store in 3 distinct variables
    long d1 = getRawDistance();
    delay(10); // Brief 10ms pause to prevent acoustic overlap (echoes)
    long d2 = getRawDistance();
    delay(10);
    long d3 = getRawDistance();
    
    // Step 3: Sort the values mathematically from lowest to highest using conditionals
    long temp;
    if (d1 > d2) { temp = d1; d1 = d2; d2 = temp; }
    if (d2 > d3) { temp = d2; d2 = d3; d3 = temp; }
    if (d1 > d2) { temp = d1; d1 = d2; d2 = temp; }
    
    // Step 4: Select the central value (the median), which is now stored in d2
    long medianDistance = d2;
    
    // Step 5: Send strictly the median value formatted as "Angle,Distance"
    Serial.print(i);
    Serial.print(",");
    Serial.println(medianDistance);
    
    // 4. TIMING ADJUSTMENT
    // We reduced the original delay(30) to 10 because we already spent ~20ms taking readings
    delay(10); 
  }
  
  // Second loop: sweep from 180 to 0 degrees (return)
  for(i = 180; i >= 0; i--) {
    // Tell the motor to go to the current degree
    miMotor.write(i);
    
    // Step 1 & 2: Launch 3 ultra-fast pulses and store in 3 distinct variables
    long d1 = getRawDistance();
    delay(10);
    long d2 = getRawDistance();
    delay(10);
    long d3 = getRawDistance();
    
    // Step 3: Sort the values mathematically from lowest to highest using conditionals
    long temp;
    if (d1 > d2) { temp = d1; d1 = d2; d2 = temp; }
    if (d2 > d3) { temp = d2; d2 = d3; d3 = temp; }
    if (d1 > d2) { temp = d1; d1 = d2; d2 = temp; }
    
    // Step 4: Select the central value (the median), which is now stored in d2
    long medianDistance = d2;
    
    // Step 5: Send strictly the median value formatted as "Angle,Distance"
    Serial.print(i);
    Serial.print(",");
    Serial.println(medianDistance);
    
    // 4. TIMING ADJUSTMENT
    delay(10);
  }
}