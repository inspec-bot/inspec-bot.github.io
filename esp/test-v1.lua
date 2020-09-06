#include <ESP8266WiFi.h>
#define LED D0                  //กำหนดขาที่ต่อ LED เป็นขา D1
const char* ssid = "A-lab";               //กำหนด SSID (อย่าลืมแก้เป็นของตัวเอง)
const char* password = "*";     //กำหนด Password(อย่าลืมแก้เป็นของตัวเอง)
unsigned char power_ac=0;
unsigned char temp_ac=25;
unsigned char fan_ac=3;
unsigned char swing_ac=4;

WiFiServer server(80);              //กำหนดใช้งาน TCP Server ที่ Port 80
 
void setup() {
  Serial.begin(115200);             //เปิดใช้ Serial
  pinMode(LED, OUTPUT);         //กำหนด Pin ที่ต่อกับ LED เป็น Output
  Serial.println();
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);
  WiFi.begin(ssid, password);           //เชื่อมต่อกับ AP
  while (WiFi.status() != WL_CONNECTED)     //รอการเชื่อมต่อ
  {
        delay(500);
        Serial.print(".");
  }
  
  IPAddress local_ip = {192,168,137,100};   //ตั้งค่า IP
  IPAddress gateway={192,168,137,1};    //ตั้งค่า IP Gateway
  IPAddress subnet={255,255,255,0};   //ตั้งค่า Subnet
  WiFi.config(local_ip,gateway,subnet);   //setค่าไปยังโมดูล
  
  Serial.println("");
  Serial.println("WiFi connected");     //แสดงข้อความเชื่อมต่อสำเร็จ  
  server.begin();                   //เปิด TCP Server
  Serial.println("Server started");
  Serial.println(WiFi.localIP());           // แสดงหมายเลข IP ของ Server
}
 
void loop() {
  WiFiClient client = server.available();       //รอรับ การเชื่อมต่อจาก Client
  if (!client) {            //ถ้าไม่มี Client เข้ามาให้เริ่มกับไปวน loop รอรับใหม่
    return;
  }
   
  Serial.println("new client");
  while(!client.available())
  {
    delay(1);
  }
  String req = client.readStringUntil('\r');        //อ่านค่าที่ได้รับจากclient จากข้อมูลแรกถึง ‘\r’ 
  Serial.println(req);              //แสดงค่าที่ได้รับทาง Serial
  client.flush();
  
  if (req.indexOf("/acoff") != -1)  
  {
    power_ac=0;                 
    digitalWrite(LED,LOW);         
  }
  else if(req.indexOf("/acon") != -1)     
  {
    power_ac=1;   
    digitalWrite(LED,HIGH);  
  }
  else if(req.indexOf("/ac19") != -1)     
  {
    temp_ac=19;   
    digitalWrite(LED,LOW);  
  }
  else if(req.indexOf("/ac20") != -1)     
  {
    temp_ac=20;   
    digitalWrite(LED,HIGH);  
  }
  else if(req.indexOf("/ac21") != -1)     
  {
    temp_ac=21;   
    digitalWrite(LED,LOW);  
  }
  else if(req.indexOf("/ac22") != -1)     
  {
    temp_ac=22;   
    digitalWrite(LED,LOW);  
  }
  else if(req.indexOf("/ac23") != -1)     
  {
    temp_ac=23;   
    digitalWrite(LED,HIGH);  
  }
  else if(req.indexOf("/ac24") != -1)     
  {
    temp_ac=24;   
    digitalWrite(LED,LOW);  
  }
  else if(req.indexOf("/ac25") != -1)     
  {
    temp_ac=25;   
    digitalWrite(LED,LOW);  
  }
  else if(req.indexOf("/ac26") != -1)     
  {
    temp_ac=26;   
    digitalWrite(LED,HIGH);  
  }
  else if(req.indexOf("/ac27") != -1)     
  {
    temp_ac=27;   
    digitalWrite(LED,LOW);  
  }
  else if(req.indexOf("/ac28") != -1)     
  {
    temp_ac=28;   
    digitalWrite(LED,HIGH);  
  }
  else if(req.indexOf("/fan1") != -1)     
  {
    fan_ac=1;   
    digitalWrite(LED,LOW);  
  }
  else if(req.indexOf("/fan2") != -1)     
  {
    fan_ac=2;   
    digitalWrite(LED,HIGH);  
  }
  else if(req.indexOf("/fan3") != -1)     
  {
    fan_ac=3;   
    digitalWrite(LED,LOW);  
  }
  else if(req.indexOf("/swing1") != -1)     
  {
    swing_ac=1;   
    digitalWrite(LED,HIGH);  
  }
  else if(req.indexOf("/swing2") != -1)     
  {
    swing_ac=2;   
    digitalWrite(LED,LOW);  
  }
  else if(req.indexOf("/swing3") != -1)     
  {
    swing_ac=3;   
    digitalWrite(LED,HIGH);  
  }
  Serial.println((String)"power:"+power_ac+" temp:"+temp_ac+" fan:"+fan_ac+" swing:"+swing_ac);
  
//เก็บ Code HTML ลงในตัวแปรสตริง web
  String web = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n";
  web += "<html>\r\n";
  web += "<body>\r\n";
  web += "<h1>AC Status</h1>\r\n";
  web += "<p>\r\n";
  if(power_ac==1) // ตรวจเช็คสถานะของ LED ว่า On หรือ Off
      web += "AC Power: On\r\n";
  else
      web += "AC Power: Off\r\n";
  web += "</p>\r\n";
  
  web +="<p>Temperature: ";
  web +=(int)temp_ac;
  web +=" C</p>";
  
  web +="<p>Fan Speed: ";
  web +=(int)fan_ac;
  
  web +="<p>Swing Mode: ";
  web +=(int)swing_ac;

  web += "</body>\r\n";
  web += "</html>\r\n";
  client.print(web);    //ส่ง HTML Code ไปยัง client
}
