// 温度湿度センサーからのデータをRaspberry Piに送信する
#include "DHT.h"
#include <Arduino.h>
#include <U8x8lib.h>

WAITING_TIME = 60000; // 送信間隔の設定（ms）

int sensorpin = A6; // センサーのピン番号
int sensorValue = 0;
//　LEDとボタンのピン番号
const int buttonPin = 6;  // ボタンのピン番号
const int ledPin = 4;     // LEDのピン番号
// DHTセンサーのタイプを定義
#define DHTTYPE DHT20      // DHT 20
DHT dht(DHTTYPE);  // DHTセンサーのインスタンスを作成

U8X8_SSD1306_128X64_NONAME_HW_I2C u8x8(/* reset=*/ U8X8_PIN_NONE);
int button_state = 0;   // ボタンの状態
int sendState = 0;    // データ送信状態

void setup() {
    pinMode(ledPin, OUTPUT);
    pinMode(buttonPin, INPUT);
    pinMode(sensorpin, INPUT);

    Serial.begin(9600);
//  Serial.println("DHTxx test!");

    Wire.begin();
    dht.begin();
    u8x8.begin();
    u8x8.setPowerSave(0); 
    u8x8.setFlipMode(1);
}
 
void loop() {
    float temp, humi;

    temp = float( dht.readTemperature() );
    humi = float( dht.readHumidity() );
    sensorValue = analogRead(sensorpin);

    if( sendState == 1 ) {
      // 温度データを送信
      Serial.print("Temperature=");
      Serial.print(temp);
      Serial.print(":");
      // 湿度データを送信
      Serial.print("Humidity=");
      Serial.print(humi);
      Serial.print(":");
      // 光センサーのデータを送信
      Serial.print("Light=");
      Serial.print(sensorValue);
      Serial.println("");
    }
    
    u8x8.setFont(u8x8_font_chroma48medium8_r);
    u8x8.clearDisplay();

    u8x8.setCursor(0, 0);
    if( sendState == 1) {
      u8x8.print("SENDING");
    } else {
      u8x8.print("STOPPED");
    }      
    u8x8.setCursor(0, 2);
    u8x8.print("Temp : ");
    u8x8.print(temp);
    u8x8.print("C");
    u8x8.setCursor(0, 3);
    u8x8.print("Humid: ");
    u8x8.print(humi);
    u8x8.print("%");
    u8x8.setCursor(0, 4);
    u8x8.print("Light: ");
    u8x8.print(sensorValue);
    u8x8.refreshDisplay();

  // ボタンの状態を読み取る
  // ボタンが押されたらデータ送信状態を切り替える
  // ボタンが押されたらLEDを点灯
    button_state = digitalRead(buttonPin);

  if (button_state == HIGH) {
    if(sendState == 0 ) {
      sendState = 1;
    } else {
      sendState = 0;
    }
    digitalWrite(ledPin, sendState);   // LEDを点灯/消灯
  }

  delay(WAITING_TIME); // 送信間隔を待つ
}