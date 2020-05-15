#include <Servo.h>
#include <ESP8266WiFi.h>
#include <WiFiUdp.h>
#include <config.h>

WiFiUDP Udp;
Servo motor;
Servo steer;

struct receive { //data to receive
  volatile int32_t cmd; 
  volatile int32_t val;
};
struct receive bytes;

byte buf[8];


void setup() {
  Serial.begin(115200);
  Serial.println();

  Serial.printf("Connecting to %s ", ssid);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED)
  {
    delay(500);
    Serial.print(".");
  }
  Serial.println(" connected");
  Udp.begin(localUdpPort);
  Serial.printf("Now listening at IP %s, UDP port %d\n", WiFi.localIP().toString().c_str(), localUdpPort);
  motor.attach(5); // pin D1
  steer.attach(4); // pin D2
  
  motor.write(90); // init ESC
  steer.write(90); // center steering

  // wait for ESC to initialize
  delay(2000); 
}

void loop() {
  int packetSize = Udp.parsePacket();
  if (packetSize) {
    Udp.read(buf, 8);
    memmove(&bytes,buf,sizeof(bytes)); 
    if (bytes.cmd == 1) {
        motor.write(bytes.val);
    }
    if (bytes.cmd == 2) {
        steer.write(bytes.val);
    }
  }
}
