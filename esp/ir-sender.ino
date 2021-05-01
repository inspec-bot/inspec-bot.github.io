#include <Arduino.h>
#include <IRremoteESP8266.h>
#include <IRsend.h>
#include <ir_Gree.h>
#include <ESP8266WiFi.h>
const char* ssid = "Test";
const char* password = "password";
unsigned char power_ac=1;
unsigned char temp_ac=25;
unsigned char temp_aco=25;
unsigned char fan_ac=3;
unsigned char swing_ac=4;
const char* drop_noti="";
WiFiServer server(80);      
const uint16_t kIrLed = 4;  
IRGreeAC ac(kIrLed);  
void setup() {
  WiFi.begin(ssid, password);           
  while (WiFi.status() != WL_CONNECTED)     
  {
        delay(500);
  }
  IPAddress local_ip = {192,168,137,x};
  IPAddress gateway={192,168,137,x};
  IPAddress subnet={255,255,255,0};
  WiFi.config(local_ip,gateway,subnet);   
  server.begin();                   
  ac.begin();
  delay(200);
  ac.on();
  ac.setFan(3);
  ac.setMode(kGreeCool); 
  ac.setSwingVertical(false, kGreeSwingDown);
  ac.setXFan(false);
  ac.setLight(true);
  ac.setSleep(false);
  ac.setTurbo(false);
}
void loop() {
  temp_aco = temp_ac;
  WiFiClient client = server.available();       
  if (!client) {            
    return;
  }
  while(!client.available())
  {
    delay(1);
  }
  String req = client.readStringUntil('\r');        
  client.flush();
  if (req.indexOf("/acoff") != -1)
  {
    power_ac=0;
    ac.off();
  }
  if(req.indexOf("/acon") != -1)     
  {
    power_ac=1;
    ac.on();
  }
  if(req.indexOf("/ac18") != -1)     
  {
    temp_ac=18;
  }
  if(req.indexOf("/ac19") != -1)     
  {
    temp_ac=19;   
  }
  if(req.indexOf("/ac20") != -1)     
  {
    temp_ac=20;   
  }
  if(req.indexOf("/ac21") != -1)     
  {
    temp_ac=21;   
  }
  if(req.indexOf("/ac22") != -1)     
  {
    temp_ac=22;   
  }
  if(req.indexOf("/ac23") != -1)     
  {
    temp_ac=23;
  }
  if(req.indexOf("/ac24") != -1)     
  {
    temp_ac=24;   
  }
  if(req.indexOf("/ac25") != -1)
  {
    temp_ac=25;
  }
  if(req.indexOf("/ac26") != -1)
  {
    temp_ac=26; 
  }
  if(req.indexOf("/ac27") != -1)
  {
    temp_ac=27;
  }
  if(req.indexOf("/ac28") != -1)
  {
    temp_ac=28;
  }
  if(req.indexOf("/ac29") != -1)
  {
    temp_ac=29;
  }
  if(req.indexOf("/ac30") != -1)
  {
    temp_ac=30;
  }
  if(req.indexOf("/drop") != -1)
  {
    drop_noti="Drop Alert !!!";
  }
  if(req.indexOf("/undrop") != -1)
  {
    drop_noti="";
  }
  if (temp_aco != temp_ac)
  {
    ac.setTemp(temp_ac);
    ac.send();
  }
  String web = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n";
  web += "<html>\r\n";
  web += "<head>\r\n";
  web += "<meta http-equiv=\"refresh\" content=\"5\">\r\n";
  web += "</head>\r\n";
  web += "<body>\r\n";
  web += "<h1>AC Status</h1>\r\n";
  web += "<p>\r\n";
  if(power_ac==1)
      web += "AC Power: On\r\n";
  else
      web += "AC Power: Off\r\n";
  web += "</p>\r\n";
  web +="<p>Temperature: ";
  web +=(int)temp_ac;
  web +=" C</p>";
  web +="<p>Fan Speed: ";
  web +=(int)fan_ac;
  web +="</p>";
  web +="<p>Swing Mode: ";
  web +=(int)swing_ac;
  web +="</p>";
  web +="<h2>";
  web +=(char*)drop_noti;
  web +="</h2>";
  web += "</body>\r\n";
  web += "</html>\r\n";
  client.print(web);    
}
