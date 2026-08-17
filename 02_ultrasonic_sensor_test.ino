// Define the pins for the ultrasonic sensor (you can change these if needed)
const int trigPin = 10;
const int echoPin = 11;

// Variables to store the time duration and the calculated distance
long duration;
long distance;

void setup() {
  // Configure the Trig pin as an output
  pinMode(trigPin, OUTPUT);
  
  // Configure the Echo pin as an input
  pinMode(echoPin, INPUT);
  
  // Initialize the Serial Monitor at 9600 baud rate
  Serial.begin(9600);
}

void loop() {
  // 1. THE TRIGGER: Clear the Trig pin first to ensure a clean pulse
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  
  // Send a 10-microsecond HIGH pulse to trigger the sensor
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  
  // 2. THE LISTENER: Wait for the echo and get the time in microseconds
  duration = pulseIn(echoPin, HIGH);
  
  // Calculate the distance in centimeters
  // Formula: Distance = (Time x Speed of Sound) / 2
  // Speed of sound is 0.034 cm/us. We divide by 2 because of the round trip (ping and pong).
  distance = duration * 0.034 / 2;
  
  // 3. THE SERIAL MONITOR: Print the result to the screen
  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println(" cm");
  
  // Wait a short moment before taking the next measurement
  delay(100);
}