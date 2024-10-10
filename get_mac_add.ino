/*#ifdef ESP32
  #include <WiFi.h>
#else
  #include <ESP8266WiFi.h>
#endif

void setup(){
  Serial.begin(9600);
  Serial.println();
  Serial.print("ESP Board MAC Address:  ");
  Serial.println(WiFi.macAddress());
}
 
void loop(){

}*/
#include <WiFi.h>

void setup() {
  Serial.begin(115200);

  // Get the MAC address
  byte mac[6];
  WiFi.macAddress(mac);

  // Print the MAC address
  Serial.print("MAC Address:");
  for (int i = 0; i < 5; i++) {
    Serial.print(mac[i], HEX);
    Serial.print(":");
  }
  Serial.print(mac[5], HEX);
  Serial.println();
}

void loop() {
  // No additional processing needed
}
