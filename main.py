import datetime

from utils import calculate_saturdays, send_slack_message


def main():
    # 実行
    current_year = datetime.datetime.now().year
    current_month = datetime.datetime.now().month
    first_saturday, _ = calculate_saturdays(current_year, current_month)

    # 特定のユーザーのDMチャンネルIDを指定
    user_dm_channel_id = "C04N08LUDCL"

    # 第一土曜日のアジェンダ募集のメッセージを送信
    send_slack_message(user_dm_channel_id, "テスト:第一土曜日のアジェンダを募集してください。")


if __name__ == "__main__":
    main()
