from function_pkg import data_receive_from_arduino
from function_pkg import data_check
from function_pkg import send_mail
from function_pkg import data_save_db

# RaspberryPi側のメインプログラム（センサー機能）
def main():
    try:
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

    except KeyboardInterrupt:
        pass

    except Exception as e:
        print(f"エラーが発生しました: {e}")
    finally:
        print("プログラムを終了します。")

if __name__ == '__main__':
    main()
    print("THSenseシステムが起動しました。")