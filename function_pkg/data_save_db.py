import datetime
import socket
import pymysql
from dotenv import load_dotenv
import os

# .envファイルの読み込み
load_dotenv()

db_ip_addr=os.getenv("DB_IP_ADDRESS") # データベースのIPアドレスを指定

# データベースに温度と湿度のデータを保存する関数
def put_data_record( temp,humid):
  id = socket.gethostname()         # ホスト名をIDとして使用
  dt = datetime.datetime.today()    # 現在の日時を取得
  db_table = os.getenv("DB_TABLE")  # テーブル名を取得
  print( 'ID=%s  DateTime=%s  Temp=%.2f  Humidity=%.2f' %(id, dt, temp, humid) )
  try:
    connection = pymysql.connect(
       host=db_ip_addr,
       user=os.getenv("DB_USER"),
       password=os.getenv("DB_PASSWORD"),
       db=os.getenv("DB_NAME"),
       charset="utf8"
       )
    with connection.cursor() as cursor:
      sql = "INSERT INTO "+db_table+" (id, dt, temp, humid) VALUES(%s, %s, %s, %s)"
      cursor.execute( sql, (id, dt, temp, humid))
    connection.commit()
    print("    Data commited.")
  except Exception as e:
        print("DB Access Error!", e)
  finally:
      if 'connection' in locals():  # connectionが存在する場合のみclose
          connection.close()

if __name__ == '__main__':
    try:
        temp = float(input("Enter Temperature: "))
        humid = float(input("Enter Humidity: "))
        put_data_record(temp, humid)
    except KeyboardInterrupt:
        pass