import smtplib
import json
import argparse
from email.message import EmailMessage

# アカウント情報を読み込み
with open("accounts.json", "r") as f:
    accounts = json.load(f)

# CLI引数を処理
parser = argparse.ArgumentParser()
parser.add_argument("--to", required=True, help="送信先メールアドレス")
parser.add_argument("--message", required=True, help="送信するメッセージ内容")
parser.add_argument("--count", type=int, required=True, help="送信する回数")
args = parser.parse_args()

# メール送信処理
for i in range(args.count):
    acc = accounts[i % len(accounts)]
    msg = EmailMessage()
    msg.set_content(args.message)
    msg["Subject"] = "Auto Message"
    msg["From"] = acc["email"]
    msg["To"] = args.to

    try:
        with smtplib.SMTP(acc["smtp_server"], acc["smtp_port"]) as smtp:
            smtp.starttls()
            smtp.login(acc["email"], acc["password"])
            smtp.send_message(msg)
        print(f"[成功] {acc['email']} → {args.to}")
    except Exception as e:
        print(f"[失敗] {acc['email']} → {args.to} | {str(e)}")