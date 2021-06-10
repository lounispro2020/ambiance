#include "DHT.h"
#include <WiFiNINA.h> 
#define DHTPIN 7// broche ou l'on a branche le capteur
#define DHTTYPE DHT11 // DHT 11

DHT dht(DHTPIN, DHTTYPE);//déclaration du capteur


char ssid[] = "AMBIANCE" ; //ssid du wifi
char pass[] = "testtest";

int status = WL_IDLE_STATUS;
char server[] = "192.168.10.1";

String postData;
String postVariable = "temp=";

WiFiClient client;
 
void setup()
{
 Serial.begin(9600);

 while (status != WL_CONNECTED) {
  Serial.print("Tentative de connexion  au serveur:");
  Serial.print(ssid);
  status = WiFi.begin(ssid,pass);
  delay(2000);
  
  }

 Serial.println("SSID: ");
 Serial.println(WiFi.SSID());
 IPAddress ip = WiFi.localIP();
 IPAddress gateway = WiFi.gatewayIP();
 Serial.print("IP Address:");
 Serial.println(ip);
 
 Serial.println("DHTambiance test!");
 dht.begin();

}



void loop(){
  int readig = analogRead(DHTPIN);
 
 delay(5000);
 
// La lecture du capteur prend 250ms
// Les valeurs lues peuvet etre vieilles de jusqu'a 2 secondes (le capteur est lent)
 float t = dht.readTemperature();//on lit la temperature en celsius (par defaut)
 
 if (isnan(t)){
   Serial.println("Failed to read from DHT sensor!");
   return;}

    
    String postData = "{\"VALEUR_TEMP\": \"" + String(t) +"\"}"; 
    if (client.connect(server, 8000)){
    client.println("POST /temp/ HTTP/1.1");
    client.println("Host: 192.168.10.1");
    client.println("Content-Type: application/json");
    client.print("Content-Length: ");
    client.println(postData.length());
    client.println();
    client.print(postData);
 } else Serial.println("non");

  if (client.connected()){
      client.stop();
    }
  Serial.println(postData);

}
