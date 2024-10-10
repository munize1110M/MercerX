// Base ESP8266
#include <ESP8266WiFi.h>
#include <PubSubClient.h>
//#include <WiFi.h>
PubSubClient MQTT_CLIENT;
WiFiClient WIFI_CLIENT;
void setup() {

  Serial.begin(9600);

  // Attempt to connect to a RPI WIFI
  WiFi.begin("rpi_netreg", NULL);

  // Keeps checking connection status till connected
  while (WiFi.status() != WL_CONNECTED) {
      delay(500);
  }

  // Print the IP address of your module
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}
// This function connects to the MQTT broker
void reconnect() {
  // Set our MQTT broker address and port
  MQTT_CLIENT.setServer("129.161.165.207", 1883);
  MQTT_CLIENT.setClient(WIFI_CLIENT   );

  // Loop until we're reconnected
  while (!MQTT_CLIENT.connected()) {
    // Attempt to connect
    Serial.println("Attempt to connect to MQTT broker");
    MQTT_CLIENT.connect("esp8266_test");

    // Wait some time to space out connection requests
    delay(3000);
  }

  Serial.println("MQTT connected");
}


void loop() {
  // Check if we're connected to the MQTT broker
  if (!MQTT_CLIENT.connected()) {
    // If we're not, attempt to reconnect
    reconnect();
  }

  // Publish a message to a topic
  MQTT_CLIENT.publish("home/sensors", "Hello world!");


  


  delay(5000);
}
