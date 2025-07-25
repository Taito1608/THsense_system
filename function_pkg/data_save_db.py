import datetime
import socket
import pymysql
from sqlalchemy.orm import Session
from db.database import SessionLocal  # セッション作成関数（環境に応じて変更してください）
from db.models import TH_tbl
from dotenv import load_dotenv
import os

# .envファイルの読み込み
# load_dotenv()

# db_ip_addr=os.getenv("DB_IP_ADDRESS") # データベースのIPアドレスを指定

def put_data_record(temp: float, humid: float):
  id = socket.gethostname()
  dt = datetime.datetime.now()

  session: Session = SessionLocal()
  try:
      new_record = TH_tbl(id=id, dt=dt, temp=temp, humid=humid)
      session.add(new_record)
      session.commit()
      print(f"ID={id}  DateTime={dt}  Temp={temp:.2f}  Humidity={humid:.2f}")
      print("    Data committed.")
  except Exception as e:
      session.rollback()
      print("DB Access Error!", e)
  finally:
      session.close()

"""
# データベースに温度と湿度のデータを保存する関数(クエリを直接実行)
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
"""

if __name__ == '__main__':
    try:
        temp = float(input("Enter Temperature: "))
        humid = float(input("Enter Humidity: "))
        put_data_record(temp, humid)
    except KeyboardInterrupt:
        pass