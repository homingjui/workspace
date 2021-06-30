#include <Wire.h>
#include <sbus.h>
#define SBUS_PIN 13
#include <JY901.h>
#include <Servo.h>

Servo Xservo;
Servo Yservo;

int servo_x_min = 60;
int servo_x_max = 170;
int Xservo_pin = 12;
int Yservo_pin = 11;

#define SLAVE_ADDRESS 0x04
int state[4] = {
  0, 0, 0, 0};
int n = 0;
int send_n = 0;

int voltage_pin = A2;

int gyroXH = 0;
int gyroXL = 0;
int gyroYH = 1;
int gyroYL = 1;
int gyroZH = 2;
int gyroZL = 2;
int accXH = 3;
int accXL = 3;
int accYH = 4;
int accYL = 4;
int accZH = 5;
int accZL = 5;
int rollH = 6;
int rollL = 6;
int pitchH = 7;
int pitchL = 7;
int yawH = 8;
int yawL = 8;
uint8_t send_buffer[20];

int pinused[] = {
  41, 43, 45, 40, 42, 44,23};
int left1 = 41;
int left2 = 43;
int leftpwm = 45;

int right1 = 40;
int right2 = 42;
int rightpwm = 44;

int motor = 15;

SBUS sbus;
int t8s[8];
int t8ss[8];
int t8sss[8];
int max_del = 500;
int min_pwm = 40;
int max_pwm = 0;
float sampling = 25;


unsigned long time;
boolean t8s5 = false;

void setup() {
  Serial.begin(115200);
  Serial2.begin(115200);
  JY901.attach(Serial2);
  Wire.begin(SLAVE_ADDRESS);

  Wire.onReceive(receiveData);
  Wire.onRequest(sendData);

  for (int i = 0; i < sizeof(pinused); i++) {
    pinMode(pinused[i], OUTPUT);
  }
  pinMode(voltage_pin, INPUT);

  sbus.begin(SBUS_PIN, sbusNonBlocking);
  for (int i = 0; i < 8; i++) t8s[i]=1500;

  Yservo.attach(Yservo_pin);
  Xservo.attach(Xservo_pin);

}
int maxx = 0;
void loop() {
  ////////////////////////////////////////////////read jy61
  JY901.receiveSerialData();
  uint16_t accX = (JY901.getAccRawX());
//  Serial.println(accX);
  accXH = accX>>8;
  accXL = (accX<<8)>>8;
  uint16_t accY = (JY901.getAccRawY());
//  Serial.println(accY);
  accYH = accY>>8;
  accYL = (accY<<8)>>8;
  uint16_t accZ = (JY901.getAccRawZ());
//  Serial.println(accZ);
  accZH = accZ>>8;
  accZL = (accZ<<8)>>8;
  uint16_t gyroX = (JY901.getGyroX()*(32768.0/2000.0))+32768;
//  Serial.println(gyroX);
  gyroXH = gyroX>>8;
  gyroXL = (gyroX<<8)>>8;
  uint16_t gyroY = (JY901.getGyroY()*(32768.0/2000.0))+32768;
//  Serial.println(gyroY);
  gyroYH = gyroY>>8;
  gyroYL = (gyroY<<8)>>8;
  uint16_t gyroZ = (JY901.getGyroZ()*(32768.0/2000.0))+32768;
//  Serial.println(gyroZ);
  gyroZH = gyroZ>>8;
  gyroZL = (gyroZ<<8)>>8;
  uint16_t roll = (JY901.getRoll()*(32768.0/180.0))+32768;
//  Serial.println(JY901.getRoll());
//  Serial.println(roll);
  rollH = roll>>8;
  rollL = (roll<<8)>>8;
  uint16_t pitch = (JY901.getPitch()*(32768.0/180.0))+32768;
//  Serial.println(JY901.getPitch());
//  Serial.println(pitch);
  pitchH = pitch>>8;
  pitchL = (pitch<<8)>>8;
  uint16_t yaw = (JY901.getYaw()*(32768.0/180.0))+32768;
//  Serial.println(JY901.getYaw());
//  Serial.println(yaw);
  yawH = yaw>>8;
  yawL = (yaw<<8)>>8;

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
      Xservo.write(int(map(t8ss[3],1025,2000,servo_x_min,servo_x_max)));
//      Serial.println(int(map(t8ss[2],1025,2000,0,180)));
    }
    else{
      if(t8ss[2]==1500){
        digitalWrite(right1,LOW);
        digitalWrite(right2,LOW);
        analogWrite(rightpwm,0);
      }
      else if(t8ss[2]>1550){/////////////////////front
        digitalWrite(right1,HIGH);
        digitalWrite(right2,LOW);
        analogWrite(rightpwm,map(abs(t8ss[2]-1550),25,450,min_pwm,max_pwm));
        //      Serial.print(" 1 ");
        //      Serial.print(map(abs(t8ss[2]-1550),25,450,min_pwm,max_pwm));
      }
      else if(t8ss[2]<1450){///////////////////////back
        digitalWrite(right1,LOW);
        digitalWrite(right2,HIGH);
        analogWrite(rightpwm,map(abs(t8ss[2]-1450),25,425,min_pwm,max_pwm));
        //      Serial.print(" 2 ");
        //      Serial.print(map(abs(t8ss[2]-1450),25,425,min_pwm+15,max_pwm));
      }
  
  
      if(t8ss[1]==1500){
        digitalWrite(left1,LOW);
        digitalWrite(left2,LOW);
        analogWrite(leftpwm,0);
      }
      else if(t8ss[1]>1550){/////////////////back
        digitalWrite(left1,HIGH);
        digitalWrite(left2,LOW);
        analogWrite(leftpwm,map(abs(t8ss[1]-1550),25,450,min_pwm,max_pwm));
        //      Serial.print(" 3 ");
        //      Serial.print(map(abs(t8ss[1]-1550),25,450,min_pwm,max_pwm));
      }
      else if(t8ss[1]<1450){////////////////front
        digitalWrite(left1,LOW);
        digitalWrite(left2,HIGH);
        analogWrite(leftpwm,map(abs(t8ss[1]-1450),25,425,min_pwm,max_pwm));
        //      Serial.print(" 4 ");
        //      Serial.print(map(abs(t8ss[1]-1450),25,425,min_pwm,max_pwm));
      }
    }
//    Serial.println();
  }

  else if(t8ss[6] == 1505){
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
  digitalWrite(left1, state[0] % 10 == 1 ? HIGH : LOW);
  digitalWrite(left2, int(state[0] / 10) == 1 ? HIGH : LOW);
  analogWrite(leftpwm, state[1]);
}
void set_left_motor() {
  digitalWrite(right1, state[2] % 10 == 1 ? HIGH : LOW);
  digitalWrite(right2, int(state[2] / 10) == 1 ? HIGH : LOW);
  analogWrite(rightpwm, state[3]);
}

void receiveData(int byteCount) {
  int n = 0;
  while (Wire.available() && n<4) {
    state[n] = Wire.read();
//    Serial.print(state[n]);
    n++;
  }
//  Serial.println(n);
//  Serial.println("!!");
}

// callback for sending data
void sendData() {
  send_buffer[0]=0;
  send_buffer[1]=255;
  send_buffer[2]=gyroXH;
  send_buffer[3]=gyroXL;
  send_buffer[4]=gyroYH;
  send_buffer[5]=gyroYL;
  send_buffer[6]=gyroZH;
  send_buffer[7]=gyroZL;
  send_buffer[8]=accXH;
  send_buffer[9]=accXL;
  send_buffer[10]=accYH;
  send_buffer[11]=accYL;
  send_buffer[12]=accZH;
  send_buffer[13]=accZL;
  send_buffer[14]=rollH;
  send_buffer[15]=rollL;
  send_buffer[16]=pitchH;
  send_buffer[17]=pitchL;
  send_buffer[18]=yawH;
  send_buffer[19]=yawL;
  Wire.write(send_buffer,20);
//  switch ( send_n ){
//  case 0:
//    Wire.write(0);
//    break;
//  case 1:
//    Wire.write(255);
//    break;
//  case 2:
//    Wire.write(analogRead(voltage_pin)/4);
//    break;
//  case 3:
//    Wire.write(gyroX);
//    break;
//  case 4:
//    Wire.write(gyroY);
//    break;
//  case 5:
//    Wire.write(gyroZ);
//    break;
//  case 6:
//    Wire.write(accX);
//    break;
//  case 7:
//    Wire.write(accY);
//    break;
//  case 8:
//    Wire.write(accZ);
//    break;
//  case 9:
//    Wire.write(roll);
//    break;
//  case 10:
//    Wire.write(pitch);
//    break;
//  case 11:
//    Wire.write(yaw);
//    break;
//  }
//  send_n += 1;
//  send_n = send_n >= 12 ? 0 : send_n;
////  Serial.print("s");
////  Serial.println(send_n);
}
