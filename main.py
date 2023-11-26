import datetime
import sys

from utils import calculate_saturdays, send_slack_message


def main():
    # 実行
    current_year = datetime.datetime.now().year
    current_month = datetime.datetime.now().month
    today = datetime.datetime.now().date()

    first_saturday, third_saturday = calculate_saturdays(
        current_year, current_month
    )  # noqa
    one_week_before_first = first_saturday - datetime.timedelta(days=7)
    one_week_before_third = third_saturday - datetime.timedelta(days=7)

    # 特定のチャンネルIDを指定
    channel_id = "C04N08LUDCL"  # randomチャンネルのID

    # メッセージの日付部分を動的に設定
    if today == one_week_before_first:
        date_str = first_saturday.strftime("%m/%d（%a）")
    elif today == one_week_before_third:
        date_str = third_saturday.strftime("%m/%d（%a）")
    else:
        sys.exit()

    message = f"""テストなので無視してください
    {date_str} 隔週mtg開催予定です。
    場所:〒150-0031 東京都渋谷区桜丘町９−１８ タカシマ桜ケ丘マンション
    日時: {date_str} 13:00-15:00

    1. 出席可否
    2. 出席可否問わずアジェンダある方はスレッドにお願いします
    """

    # メッセージを送信
    send_slack_message(channel_id, message)


if __name__ == "__main__":
    main()
