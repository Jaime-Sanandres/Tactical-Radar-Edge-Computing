#include <Servo.h>

Servo miMotor;

void setup() {
  miMotor.attach(9);
}

void loop() {
  int i;
  
  // First loop: from 0 to 180 degrees
  for(i=0; i<=180; i++) {
    miMotor.write(i);  // Moves the motor to the current angle 'i'
    delay(15);         // Waits 15 ms for the motor to reach the position
  }
  
  // Second loop: from 180 to 0 degrees (return)
  for(i=180; i>=0; i--) {
    miMotor.write(i);  // Moves the motor to the current angle 'i'
    delay(15);         // Waits 15 ms for the motor to reach the position
  }
}