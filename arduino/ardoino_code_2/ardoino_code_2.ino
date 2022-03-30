#include <Wire.h>
#include <sbus.h>
#define SBUS_PIN A1
#include <Servo.h>
#define SLAVE_ADDRESS 0x04
//Servo Xservo;
Servo Yservo;
bool debug=false;
/*
D11 -> 11
D10 -> 10
D9 -> 9
D7 -> 6
D8 -> 5
D6 -> 3
LIN1 -> 8
LIN2 -> x
LPWM -> 10
RIN1 -> A0  9
RIN2 -> x
RPWM -> 11
motor en -> 7

L-[6], R-[7]
L R |   top       |   mid   |    but
--------------------------------------------
top | hand laser  |         | hand control LR
--------------------------------------------
mid |             |         | hand control FB
--------------------------------------------
but |             auto control    

*/
///////////////////////////////pin 11 10 cannot used for pwm
int current_pin = A2;
int voltage_pin = A3;

int Xservo_pin = -1;//5;
int Yservo_pin = 3;
int laser = -1;

int left1 = A0;
int left2 = 11;
int leftpwm = 6;

int right1 = 9;
int right2 = 8;
int rightpwm = 5;

int motor = 7;

int pinused[] = {
  left1, left2, leftpwm, right1, right2, rightpwm,Xservo_pin,Yservo_pin,laser,motor};

int state[4] = {
  0, 0, 0, 0};
int n = 0;
int send_n = 0;
uint8_t send_buffer[20];

SBUS sbus;
int t8s[8];
int t8ss[8];
int t8sss[8];
int max_del = 500;
int min_pwm = 40;
int max_pwm = 0;
float sampling = 25;

int servo_x_min = 60;
int servo_x_max = 170;

unsigned long time;
boolean t8s5 = false;

void setup() {
  Serial.begin(115200);

  
  Serial.println("pin init");
  for (int i = 0; i < sizeof(pinused)/sizeof(pinused[0]); i++) {
    pinMode(pinused[i], OUTPUT);
    digitalWrite(pinused[i], LOW);
    Serial.println(pinused[i]);
  }
  pinMode(current_pin, INPUT);
  pinMode(voltage_pin, INPUT);
  Serial.println("pin init done");

  sbus.begin(SBUS_PIN, sbusNonBlocking);
  for (int i = 0; i < 8; i++) t8s[i]=1500;

  Yservo.attach(Yservo_pin);
//  Xservo.attach(Xservo_pin);/
}
int maxx = 0;
void loop() {
 
  Serial.println();
  /////////////////////////////////////////////////get t8s sbus
  if (sbus.failsafeActive()){
    digitalWrite(right1,LOW);
    digitalWrite(right2,LOW);
    analogWrite(rightpwm,0);
    digitalWrite(left1,LOW);
    digitalWrite(left2,LOW);
    analogWrite(leftpwm,0);
//    Serial.print("fail");
    return;
  }
  int temp = sbus.getChannel(9);
  if (temp != 1547 || sbus.signalLossActive()){
//    Serial.println("break");
    return;
  }
  temp = sbus.getChannel(1);
  if (temp > 1000 && abs(temp-t8s[0])<max_del ) t8s[0] = temp;
  temp = sbus.getChannel(2);
  if (temp > 1000 && abs(temp-t8s[1])<max_del ) t8s[1] = temp;
  temp = sbus.getChannel(3);
  if (temp > 1000 && abs(temp-t8s[2])<max_del ) t8s[2] = temp;
  temp = sbus.getChannel(4);
  if (temp > 1000 && abs(temp-t8s[3])<max_del ) t8s[3] = temp;
  temp = sbus.getChannel(5);
  if (temp == 1005 || temp == 1505 || temp == 2005) t8s[7] = temp;
  temp = sbus.getChannel(6);
  if (temp == 1005 || temp == 2005) t8s[5] = temp;
  temp = sbus.getChannel(7);
  if (temp == 1005 || temp == 1505 || temp == 2005) t8s[6] = temp;
  temp = sbus.getChannel(8);
  if (temp > 1000) t8s[4] = temp;
  t8s[0] = int((float(t8s[0])-sampling/2-1005)/sampling)*sampling+(sampling/2+1013);
  t8s[1] = int((float(t8s[1])-sampling/2-1005)/sampling)*sampling+(sampling/2+1013);
  t8s[2] = int((float(t8s[2])-sampling/2-1005)/sampling)*sampling+(sampling/2+1013);
  t8s[3] = int((float(t8s[3])-sampling/2-1005)/sampling)*sampling+(sampling/2+1013);
  t8s[4] = int((float(t8s[4])-sampling/2-1005)/sampling)*sampling+(sampling/2+1013);
  if( abs(t8s[0]-t8sss[0]) < abs(t8s[0]-t8ss[0]) ) t8ss[0]=t8sss[0];
  if( abs(t8s[1]-t8sss[1]) < abs(t8s[1]-t8ss[1]) ) t8ss[1]=t8sss[1];
  if( abs(t8s[2]-t8sss[2]) < abs(t8s[2]-t8ss[2]) ) t8ss[2]=t8sss[2];
  if( abs(t8s[3]-t8sss[3]) < abs(t8s[3]-t8ss[3]) ) t8ss[3]=t8sss[3]; 
  if( abs(t8s[4]-t8sss[4]) < abs(t8s[4]-t8ss[4]) ) t8ss[4]=t8sss[4];
  for (int i = 0; i < 8; i++) {
    Serial.print(t8ss[i]);
    Serial.print(",");
  }
  max_pwm = map(t8ss[4],1025,2000,min_pwm,255);
  //  Serial.print(max_pwm);
  Serial.print(analogRead(voltage_pin));
  Serial.print(",");
  Serial.print(analogRead(current_pin)*10);
  Serial.println();
  /////////////////////////////////////////////////set from nano
  if(t8ss[6] == 1005){
      set_left_motor();
      set_right_motor();
  }
  
  ////////////////////////////////////////////////////set from t8ss
  else if(t8ss[6] == 2005){
    if(t8ss[7] == 2005){
      Yservo.write(int(map(t8ss[2],1025,2000,0,180)));
//      Xservo.write(int(map(t8ss[3],1025,2000,servo_x_min,servo_x_max)));/
//      Serial.println(int(map(t8ss[2],1025,2000,0,180)));
    }
    else if(t8ss[7] == 1005){
      if(t8ss[2]>1550){/////////////////////L   front
        digitalWrite(right1,HIGH);
        digitalWrite(right2,LOW);
        int myspeed = int(map(abs(t8ss[2]-1550),25,450,min_pwm,max_pwm));
        analogWrite(rightpwm,myspeed);
        if(debug){
          Serial.print(" 1 ");
          Serial.print(myspeed);
        }
      }
      else if(t8ss[2]<1450){///////////////////////back
        digitalWrite(right1,LOW);
        digitalWrite(right2,HIGH);
        int myspeed = int(map(abs(t8ss[2]-1450),25,425,min_pwm,max_pwm));
        analogWrite(rightpwm,myspeed);
        if(debug){
          Serial.print(" 2 ");
          Serial.print(myspeed);
        }
      }
      else{
        digitalWrite(right1,LOW);
        digitalWrite(right2,LOW);
        analogWrite(rightpwm,0);
        if(debug){
          Serial.print(" R0 ");
        }
      }
  
  
      if(t8ss[1]>1550){/////////////////R     back
        digitalWrite(left1,HIGH);
        digitalWrite(left2,LOW);
        int myspeed = int(map(abs(t8ss[1]-1550),25,450,min_pwm,max_pwm));
        analogWrite(leftpwm,myspeed);
        if(debug){
          Serial.print(" 3 ");
          Serial.print(myspeed);
        }
      }
      else if(t8ss[1]<1450){////////////////front
        digitalWrite(left1,LOW);
        digitalWrite(left2,HIGH);
        int myspeed = int(map(abs(t8ss[1]-1450),25,425,min_pwm,max_pwm));
        analogWrite(leftpwm,myspeed);
        if(debug){
          Serial.print(" 4 ");
          Serial.print(myspeed);
        }
      }
      else{
        digitalWrite(left1,LOW);
        digitalWrite(left2,LOW);
        analogWrite(leftpwm,0);
        if(debug){
          Serial.print(" L0 ");
        }
      }
    }
//    Serial.println();
  }

  else if(t8ss[6] == 1505){
    if(t8ss[7] == 1005){
      if(t8ss[2]==1500){
        digitalWrite(right1,LOW);
        digitalWrite(right2,LOW);
        analogWrite(rightpwm,0);
        digitalWrite(left1,LOW);
        digitalWrite(left2,LOW);
        analogWrite(leftpwm,0);
      }
      else if(t8ss[2]>1550){/////////////////////front
        int pwm = map(abs(t8ss[2]-1550),25,450,min_pwm,max_pwm);
        int turn = map(abs(t8ss[0]-1500),25,500,0,pwm);
        digitalWrite(right1,HIGH);
        digitalWrite(right2,LOW);
        digitalWrite(left1,LOW);
        digitalWrite(left2,HIGH);
        if( t8ss[0] == 1500){
          analogWrite(leftpwm,pwm);
          analogWrite(rightpwm,pwm);
        }
        else if(t8ss[0] > 1500){
          analogWrite(leftpwm,pwm-turn);
          analogWrite(rightpwm,pwm);
        }
        else if(t8ss[0] < 1500){
          analogWrite(leftpwm,pwm);
          analogWrite(rightpwm,pwm-turn);
        }
      }
      else if(t8ss[2]<1450){///////////////////////back
        int pwm = map(abs(t8ss[2]-1450),25,425,min_pwm,max_pwm);
        int turn = map(abs(t8ss[0]-1500),25,500,0,pwm);
        digitalWrite(right1,LOW);
        digitalWrite(right2,HIGH);
        digitalWrite(left1,HIGH);
        digitalWrite(left2,LOW);
        if( t8ss[0] == 1500){
          analogWrite(leftpwm,pwm);
          analogWrite(rightpwm,pwm);
        }
        else if(t8ss[0] < 1500){
          analogWrite(leftpwm,pwm-turn);
          analogWrite(rightpwm,pwm);
        }
        else if(t8ss[0] > 1500){
          analogWrite(leftpwm,pwm);
          analogWrite(rightpwm,pwm-turn);
        }
      }
    }
  }

  if (t8s[5] == 1005){
    if(!t8s5){
      time=millis();
      t8s5 = true;
    }
  }
  else{
    if(t8s5){
      if(t8s[7] == 1005){
        if(millis()-time < 1000){
          digitalWrite(motor,LOW);
          
        }
        else{
          digitalWrite(motor,HIGH);
        }
      }

      t8s5 = false;
    }
  }

  delay(10);
  memcpy(t8sss, t8ss, sizeof(t8ss[0])*8);
  memcpy(t8ss, t8s, sizeof(t8s[0])*8);
}

void set_right_motor() {
//  digitalWrite(left1, state[0] % 10 == 1 ? HIGH : LOW);
//  digitalWrite(left2, int(state[0] / 10) == 1 ? HIGH : LOW);
//  analogWrite(leftpwm, state[1]);
}
void set_left_motor() {
//  digitalWrite(right1, state[2] % 10 == 1 ? HIGH : LOW);
//  digitalWrite(right2, int(state[2] / 10) == 1 ? HIGH : LOW);
//  analogWrite(rightpwm, state[3]);
}
