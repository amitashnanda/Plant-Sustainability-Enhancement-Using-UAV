#include <Servo.h>
#define l1 2
#define l2 3
#define r1 4
#define r2 5
int angle1=60;
int angle2=90;
int step = 5;

int incomingByte=0;
Servo s1,s2; 

void setup() {
  Serial.begin(9600);
  pinMode(l1,OUTPUT);
  pinMode(l2,OUTPUT);
  pinMode(r1,OUTPUT);
  pinMode(r2,OUTPUT);
  s1.attach(9);
  s2.attach(10);
  s1.write(60);
  s2.write(90);
}

void loop() {
  if (Serial.available() > 0) {
    incomingByte = Serial.read();
    
    if(incomingByte==102){      // forward
    digitalWrite(2,HIGH);
    digitalWrite(3,LOW);
    digitalWrite(4,HIGH);
    digitalWrite(5,LOW);
    Serial.print("f");
    }
    else if(incomingByte==98){   // backward
     digitalWrite(l1,LOW);
    digitalWrite(l2,HIGH);
    digitalWrite(r1,LOW);
    digitalWrite(r2,HIGH);
   
    }
    else if(incomingByte==108){    //left
     digitalWrite(l1,HIGH);
    digitalWrite(l2,LOW);
    digitalWrite(r1,LOW);
    digitalWrite(r2,HIGH);

    }
    else if(incomingByte==114){    // right
     digitalWrite(l1,LOW);
    digitalWrite(l2,HIGH);
    digitalWrite(r1,HIGH);
    digitalWrite(r2,LOW);
    }
    else if(incomingByte==117){    // upward   u
     angle1 -= step;
     if(angle1<0)
      angle1 =0;
      s1.write(angle1);
    }
    else if(incomingByte==100){    // downward    d
      angle1 += step;
      if(angle1>180)
      angle1=180;
      s1.write(angle1);
    }
    else if(incomingByte==121){    // camera left  x
     angle2 -= step;
     if(angle2<0)
      angle2 =0;
     s2.write(angle2);
    }
     else if(incomingByte==120){    // camera right y
      angle2 += step;
      if(angle2>180)
      angle2=180;
      s2.write(angle2);
    }
    else{                            // stop
    digitalWrite(l1,LOW);
    digitalWrite(l2,LOW);
    digitalWrite(r1,LOW);
    digitalWrite(r2,LOW);
    s2.write(90);
    }

  }
}
