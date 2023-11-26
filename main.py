import datetime
import logging

from config import channel_id
from utils import calculate_saturdays, send_slack_message

# ロギングの設定
logging.basicConfig(
    filename="slack_messaging.log",
    level=logging.INFO,
    format="%(asctime)s:%(levelname)s:%(message)s",
)


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

    # date_str = "test" # テスト用
    # if today: # テスト用
    if today == one_week_before_first or today == one_week_before_third:
        if today == one_week_before_first:
            date_str = first_saturday.strftime("%m/%d（%a）")
        else:
            date_str = third_saturday.strftime("%m/%d（%a）")

        message = f"""テスト
        {date_str} 隔週mtg開催予定です。
        場所:〒150-0031 東京都渋谷区桜丘町９−１８ タカシマ桜ケ丘マンション
        日時: {date_str} 13:00-15:00

        1. 出席可否
        2. 出席可否問わずアジェンダある方はスレッドにお願いします
        """
        send_slack_message(channel_id, message)
        logging.info(f"Message sent for {date_str}")
    else:
        logging.info("No message sent today")


if __name__ == "__main__":
    main()
