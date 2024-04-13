#include <EEPROM.h>

#define BAUD_RATE 2400
#define EEPROM_SIZE 1024

unsigned long lastTransmissionTime = 0;

void setup() {
  Serial.begin(BAUD_RATE);
}

void loop() {
  if (Serial.available()) {
    int addr = 0;
    unsigned long startTime = millis();
    while (Serial.available()) {
      char c = Serial.read();
      EEPROM.write(addr++, c);
    }
    unsigned long endTime = millis();
    unsigned long duration = endTime - startTime;
    float speed = (float)(8 * addr) / duration;
    Serial.print("Transmit speed: ");
    Serial.print(speed);
    Serial.println(" bits/second");
    lastTransmissionTime = millis();
  }
}
