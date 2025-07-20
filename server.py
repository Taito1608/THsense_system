from flask import Flask, render_template
from function_pkg.data_get_db import get_now_data, get_hour_data

app = Flask(__name__)

@app.route("/", methods=["GET"])
def display_lastdata():
    print("display_lastdataを実行しました。(to Terminal)")

    # 最新のデータを取得
    last_data = get_now_data()
    
    return render_template("index.html",last_data=last_data) 

# Flaskアプリケーションを起動
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)