#include <WiFiNINA.h>
#include <DHT11.h>
#include <ArduinoJson.h>

// WiFi parameters
const char* ssid = "xxxxxxx";
const char* password = "xxxxx";

DHT11 dht11(2);

// Server parameters
WiFiServer server(80);

void setup() {
  Serial.begin(9600);

  connectWifi();
}

void loop() {
  
  handleClient();
}

StaticJsonDocument<200> getSensorData(){

    StaticJsonDocument<200> data;

    int tempReading = 0;
    int humidityReading = 0;

    int result = dht11.readTemperatureHumidity(tempReading, humidityReading);

    if (result == 0){

      double fahrenheit = (9.0  / 5.0) * tempReading + 32;


      Serial.println(fahrenheit);

      String tempStr = String(fahrenheit) + "\u00B0F";
      String humidityStr = String(humidityReading) + "%";

      Serial.println(tempStr);
      Serial.println(humidityStr);

      data["temperature"] = tempStr;
      data["humidity"] = humidityStr;
    }
    else{
      Serial.println(DHT11::getErrorString(result));
    }

    serializeJson(data, Serial);

    return data;
}

void connectWifi(){
  // Connect to WiFi
  Serial.print("Connecting to WiFi");
  while (WiFi.begin(ssid, password) != WL_CONNECTED) {
    Serial.print(".");
    delay(1000);
  }
  Serial.println("WiFi connected");
  
  // Start server
  server.begin();
  Serial.println("Server started");

  Serial.print("Local IP Address: ");
  Serial.println(WiFi.localIP());
}

void handleClient(){

  // Check if a client has connected
  WiFiClient client = server.available();
  if (client) {
    Serial.println("Client connected");    
    
    // Read the request from the client
    String request = client.readStringUntil('\r');
    Serial.println("Request: " + request);

    String jsonData;    
    StaticJsonDocument<200> data = getSensorData();
    serializeJson(data, jsonData);

    client.println("HTTP/1.1 200 OK");
    client.println("Content-Type: application/json");    
    client.println("Connection: close"); // Close the connection after sending
    client.println();
    client.println(jsonData);
    
        
    // Close the connection
    client.stop();
    Serial.println("Client disconnected");
  }
}