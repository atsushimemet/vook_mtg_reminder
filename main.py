import datetime

from utils import calculate_saturdays, send_slack_message


def main():
    # 実行
    current_year = datetime.datetime.now().year
    current_month = datetime.datetime.now().month
    first_saturday, _ = calculate_saturdays(current_year, current_month)

    # 特定のユーザーのDMチャンネルIDを指定
    channel_id = "C04N08LUDCL"  # random

    message = """テスト
    11/18（土）隔週mtg開催予定です。
    場所:〒150-0031 東京都渋谷区桜丘町９−１８ タカシマ桜ケ丘マンション
    日時: 11/18（土）13:00-15:00

    1. 出席可否
    2. 出席可否問わずアジェンダある方はスレッドにお願いします
    """
    # 第一土曜日のアジェンダ募集のメッセージを送信
    send_slack_message(channel_id, message)


if __name__ == "__main__":
    main()
