// S0S signal in Morse code

const int ledPin1 = 13; 
const int ledPin2 = 4;

void setup() {
  pinMode(ledPin1, OUTPUT);
  pinMode(ledPin2, OUTPUT);
}

void shortBlink() {
  digitalWrite(ledPin1, HIGH);
  digitalWrite(ledPin2, HIGH);
  delay(200);
  digitalWrite(ledPin1, LOW);
  digitalWrite(ledPin2, LOW);
  delay(200);
}

void longBlink() {
  digitalWrite(ledPin1, HIGH);
  digitalWrite(ledPin2, HIGH);
  delay(600);
  digitalWrite(ledPin1, LOW);
  digitalWrite(ledPin2, LOW);
  delay(200);
}

void loop() {
  // S (... )
  shortBlink();
  shortBlink();
  shortBlink();
  delay(600); // Gap between letters

  // O (---)
  longBlink();
  longBlink();
  longBlink();
  delay(600); // Gap between letters

  // S (...)
  shortBlink();
  shortBlink();
  shortBlink();
  
  delay(3000); 
}