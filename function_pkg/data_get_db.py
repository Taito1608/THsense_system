from db.database import SessionLocal
from db.models import TH_tbl
import pymysql
from dotenv import load_dotenv
import os

# .envファイルから環境変数を読み込む
# load_dotenv()

# db_ip_addr= os.getenv("REMOTE_DB_IP_ADDRESS")   # データベースのIPアドレスを指定
# db_table  = os.getenv("DB_TABLE")               # テーブル名を取得

def get_now_data():
    session = SessionLocal()
    try:
        last_data = session.query(TH_tbl).order_by(TH_tbl.dt.desc()).limit(1).all()
        # オブジェクト → タプルへ変換
        return [ (d.id, d.dt, d.temp, d.humid) for d in last_data ]
    except Exception as e:
        print(f"DB Access Error: {e}")
    finally:
        session.close()

def get_hour_data():
    session = SessionLocal()
    try:
        hour_data = session.query(TH_tbl).order_by(TH_tbl.dt.desc()).limit(60).all()
        # オブジェクト → タプルへ変換
        return [ (d.id, d.dt, d.temp, d.humid) for d in hour_data ]
    except Exception as e:
        print(f"DB Access Error: {e}")
    finally:
        session.close()

"""(クエリを直接実行する場合のコード)
# データベースからデータを取得して表示する関数
def get_now_data():
    try:
        # データベースに接続
        connection = pymysql.connect(
            host=db_ip_addr,
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            db=os.getenv("DB_NAME"),
            charset="utf8"
        ) # データベースの接続設定
        with connection.cursor() as cursor:
            sql = "SELECT * FROM " + db_table + " ORDER BY dt DESC LIMIT 1"
            cursor.execute(sql)
            last_data = cursor.fetchall()
            return last_data
    except Exception as e:
        print(f"DB Access Error: {e}")
    finally:
        if 'connection' in locals():  # connectionが存在する場合のみclose
          connection.close()

def get_hour_data():
    try:
        # データベースに接続
        connection = pymysql.connect(
            host=db_ip_addr,
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            db=os.getenv("DB_NAME"),
            charset="utf8"
        ) # データベースの接続設定
        with connection.cursor() as cursor:
            sql = "SELECT * FROM " + db_table + " ORDER BY dt DESC LIMIT 60"
            cursor.execute(sql)
            hour_data = cursor.fetchall()
            return hour_data
    except Exception as e:
        print(f"DB Access Error: {e}")
    finally:
        if 'connection' in locals():  # connectionが存在する場合のみclose
          connection.close()
"""

if __name__ == '__main__':
    # 最新のデータを取得して表示
    last_data = get_now_data()
    print("Latest Data:")
    for data in last_data:
        sel_dt1 = data[0]
        sel_dt2 = data[1]
        sel_dt3 = data[2]
        sel_dt4 = data[3]
        print("{0},  {1},  {2},  {3}".format(sel_dt1, sel_dt2, sel_dt3, sel_dt4))

    # 過去1時間のデータを取得して表示
    print("\nData from the last hour:")
    hour_data = get_hour_data()
    for data in hour_data:
        sel_dt1 = data[0]
        sel_dt2 = data[1]
        sel_dt3 = data[2]
        sel_dt4 = data[3]
        print("{0},  {1},  {2},  {3}".format(sel_dt1, sel_dt2, sel_dt3, sel_dt4))