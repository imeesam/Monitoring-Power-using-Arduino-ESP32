
#include <ArduinoJson.h>
#include <Wire.h>
#include "ACS712.h"
#include "zmpt101b"

#define ACS712_PIN A3
#define ZMPT101B_PIN A2

ACS712  ACS(A0, 5.0, 1023, 100);

void setup() {
 
  Serial.begin(9600);
}

void loop() {
  float curr_value = ACS.mA_AC();
  int zmpt101b_value = analogRead(ZMPT101B_PIN);

  StaticJsonDocument<200> doc;
  doc["Voltage"] = zmpt101b_value;
  doc["Current"] = curr_value;

  String output;
  serializeJson(doc, output);
  Serial.println(output);

  delay(1000);
}