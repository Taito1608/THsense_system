#　THsense_system
温度・湿度センサーを用いた危険通知システム

## 使用技術
<img src="https://img.shields.io/badge/-Python-3776AB.svg?logo=python&style=plastic">　<img src="https://img.shields.io/badge/-Html5-E34F26.svg?logo=html5&style=plastic">　<img src="https://img.shields.io/badge/-Css3-1572B6.svg?logo=css3&style=plastic">　<img src="https://img.shields.io/badge/-Javascript-F7DF1E.svg?logo=javascript&style=plastic">　<img src="https://img.shields.io/badge/-Flask-000000.svg?logo=flask&style=plastic">　<img src="https://img.shields.io/badge/-Arduino-00979D.svg?logo=arduino&style=plastic">　<img src="https://img.shields.io/badge/-Raspberrypi-C51A4A.svg?logo=raspberrypi&style=plastic">

## 概要
本プロジェクトは個人開発にて作成した、温度・湿度センサーを用いた危険通知システムである。温度・湿度センサー（DHT22）の制御にはArduinoとRaspberryPiを用いている。主な機能として、センサーから取得したデータをブラウザに表示する機能、基準外の温度が検出された場合メールをユーザーに送信する機能を有している。

主な機能
- センサーから温度・湿度データを取得
- 温度の判定（基準値35度以内）
- DBにデータを保存
- メールの送信
- ブラウザに最新の温度データを表示
- 過去60件分の温度・湿度データをグラフ化し表示

## ディレクトリ構成
```
.
└── THsense_system/
    ├── function_pkg/
    │   ├── data_check.py
    │   ├── data_get_db.py
    │   ├── data_receive_from_arduino.py
    │   ├── data_save_db.py
    │   └── send_mail.py
    ├── static/
    │   └── style.css
    ├── templates/
    │   ├── layout.html
    │   ├── index.html
    │   └── hour.html
    ├── .gitignore
    ├── sensor.py
    ├── server.py
    ├── data_send_to_raspi.ino
    └── README.md
```