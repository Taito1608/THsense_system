from function_pkg import data_receive_from_arduino
from function_pkg import data_check
from function_pkg import send_mail
from function_pkg import data_save_db
import serial

# ポートの設定
# 注意: ポート名は環境に応じて変更してください
ser = serial.Serial('/dev/ttyUSB0', 9600)

# RaspberryPi側のメインプログラム（センサー機能）
def main():
    while True:
        # Arduinoからデータを受信
        temp, humid = data_receive_from_arduino.read_usb()
        
        # 温度のチェック
        if data_check.check_temperature(temp):
            print('【危険】基準外の温度です。')
            send_mail.send_mail()  # メール送信
        else:
            print('温度は基準内です。')

        # データベースに保存
        data_save_db.put_data_record(temp, humid)

if __name__ == '__main__':
    try:
        main()
        print("THSenseシステムが起動しました。")
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(f"エラーが発生しました: {e}")
    finally:
        print("プログラムを終了します。")
        ser.close()