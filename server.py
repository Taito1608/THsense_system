from flask import Flask, render_template
from function_pkg.data_get_db import get_now_data, get_hour_data

app = Flask(__name__)

@app.route("/", methods=["GET"])
def display_lastdata():
    print("display_lastdataを実行しました。(to Terminal)")

    # 最新のデータを取得
    last_data = get_now_data()
    
    return render_template("index.html",last_data=last_data) 

@app.route("/hour", methods=["GET"])
def display_hourdata():
    print("display_hourdataを実行しました。(to Terminal)")

    # 過去60件分のデータを取得
    hour_data = get_hour_data()

    # データを整形してグラフ用に準備
    graph_data = [
        [dt.strftime("%Y %m/%d %H:%M"), temp, hum]
        for _, dt, temp, hum in hour_data
    ]
    
    return render_template("hour.html", graph_data=graph_data)

# Flaskアプリケーションを起動
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)