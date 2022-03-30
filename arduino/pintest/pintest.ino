int test=7;

void setup() {
  // put your setup code here, to run once:
  pinMode(test,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(test,HIGH);
  delay(1000);
  digitalWrite(test,LOW);
  delay(1000);
}
