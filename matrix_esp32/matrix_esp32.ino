#include <Wire.h>

#define I2C_SLAVE_ADDR 0x08  // Dirección del esclavo ESP32

void receiveEvent(int bytes);

void setup() {
    Wire.begin(I2C_SLAVE_ADDR);  // Inicializa el ESP32 como esclavo
    Wire.onReceive(receiveEvent);  // Maneja datos recibidos
    Serial.begin(115200);
}

void loop() {
    delay(100);
}

// Función que se ejecuta cuando el maestro envía datos
void receiveEvent(int bytes) {
    if (Wire.available()) {
        int received = Wire.read();  // Leer un solo byte
        Serial.print("Número recibido: ");
        Serial.println(received);
    }
}
