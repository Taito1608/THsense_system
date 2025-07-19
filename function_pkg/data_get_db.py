import pymysql.cursors
from dotenv import load_dotenv
import os

# .envファイルから環境変数を読み込む
load_dotenv()

db_ip_addr= os.getenv("REMOTE_DB_IP_ADDRESS")   # データベースのIPアドレスを指定
db_table  = os.getenv("DB_TABLE")               # テーブル名を取得

# データベースからデータを取得して表示する関数
def get_data_from_db():
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
            sql = "SELECT * FROM " + db_table + " ORDER BY id DESC LIMIT 60"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    except Exception as e:
        print(f"DB Access Error: {e}")
    finally:
        if 'connection' in locals():  # connectionが存在する場合のみclose
          connection.close()

if __name__ == '__main__':
    result = get_data_from_db()
    for data in result:
        sel_dt1 = data[0]
        sel_dt2 = data[1]
        sel_dt3 = data[2]
        sel_dt4 = data[3]
        print("{0},  {1},  {2},  {3}".format(sel_dt1, sel_dt2, sel_dt3, sel_dt4))