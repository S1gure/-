# ツールの使い方

## 送信方法
- python main.py --to 宛先メールアドレス --message "本文メッセージ" --count 送信回数

## 主な機能

- 複数の送信アカウント（Gmailなど）を使い、順番にメールを送信
- 宛先・本文・送信回数を自由に指定可能
- 実行ログをターミナルに表示
- Gmail、Outlook、YahooなどのSMTPに対応

---

## 必要環境

- Python 3.7 以上
- インターネット接続
- Gmailなどの場合は「アプリパスワード」が必要（通常パスワードではログイン不可）

---

## セットアップ手順

1. リポジトリをクローンまたはZIPでダウンロード・解凍：

```bash
git clone https://github.com/yourname/multi-mail-sender.git
cd multi-mail-sender