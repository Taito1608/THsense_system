import serial

# ポートの設定
# 注意: ポート名は環境に応じて変更してください
ser = serial.Serial('/dev/ttyUSB0', 9600)

# Arduinoからのデータを受信する関数
def read_usb():
  in_txt=ser.readline()
  while ser.in_waiting:
    in_txt = in_txt + ser.readline()
  print("")
  print( 'Input_Text: ', in_txt )

  # 受信したデータを分割
  txt1 = in_txt.split(b':')
  txt2 = txt1[0].split(b'Temperature=')
  txt3 = txt1[1].split(b'Humidity=')
  txt4 = txt3[1].split(b'\r')

  # 文字列から数値に変換
  temp = float( txt2[1] )
  humid = float( txt3[1] )

  return temp,humid

if __name__ == '__main__':
  try:
    while True:
      temp, humid = read_usb()
      print('Temperature: ', temp, 'C')
      print('Humidity: ', humid, '%')
      print('--------------------------')
  except KeyboardInterrupt:
    pass
  ser.close()