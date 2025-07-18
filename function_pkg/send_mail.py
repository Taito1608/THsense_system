from email.mime.text import MIMEText
import smtplib
from dotenv import load_dotenv
import os

# メールを送信する関数
def send_mail():
    # .envファイルの読み込み
    load_dotenv()
    
    # SMTP認証情報
    account = os.getenv("MAIL_ACCOUNT")
    password = os.getenv("MAIL_PASSWORD")
    
    # 送受信先
    to_email = os.getenv("TO_MAIL")
    from_email = os.getenv("FROM_MAIL")
    
    # MIMEの作成
    subject = "【重要】THSenseシステムからの通知"
    message = "基準外の温度が検出されました。" \
    "<br>詳細はブラウザを確認してください。"
    msg = MIMEText(message, "html")
    msg["Subject"] = subject
    msg["To"] = to_email
    msg["From"] = from_email
    
    # メール送信処理
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(account, password)
    server.send_message(msg)
    server.quit()
 
if __name__ == "__main__":
    send_mail()
    print("メールを送信しました。")