const int sensorPin = A0;
const float baselineTemp = 20.0;

void setup() {
   Serial.begin(9600);
  
}

void loop() {

 float temp = takeTemp();
 
// float targetTemp = getTargetTemp();
 
 void runFurnace(float temp, float targetTemp);


}


float takeTemp() {
 int sensorVal = analogRead(sensorPin);
 float voltage = (sensorVal/1024.0)*5.0;
 float temperature = (voltage - .5) * 100;
 float fTemp = ((9.0/5)*temperature+32);
Serial.println(fTemp);

}

float getTargetTemp() {
 float targetTemp = 0;
 
 if (Serial.available() > 0) {
   float targetTemp = Serial.read();
 }
 return targetTemp;
  
 
 
 
}

void runFurnace(float temp, float targetTemp){
  targetTemp=100;
  if(targetTemp<temp)
   pinMode(12,OUTPUT);

}
