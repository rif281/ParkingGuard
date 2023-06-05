int front = 10;
int back = 7;

String msg;
char flag = 'Z';

void setup() {
  Serial.begin(9600);
  pinMode(front,INPUT);
  pinMode(back, INPUT);
}



void loop() {

  if(flag = 'Z'){
    readSensors();
  }
  else{
    Serial.print(flag);
    readSerialPort();

  } 
}
void readSensors(){
    
  if (digitalRead(front) == HIGH){
    msg = "Front hit detcted!\n";
    sendData();
  }
  else if (digitalRead(back) == HIGH){
    msg = "Back hit detected!\n";
    sendData();
  }
  else{
    msg ="Non detection\n";
    sendData();
  }
  
}

void readSerialPort(){

  if(Serial.available()){
    while(Serial.available() > 0){
      flag += (char)Serial.read();
    }
    Serial.flush();
    
  }
}

void sendData(){
  Serial.print(msg);
  msg = "None Detected\n";
  delay(150);
}
