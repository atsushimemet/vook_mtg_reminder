# import pytest
from datetime import datetime
from unittest.mock import patch

from utils import calculate_saturdays, set_slack_reminder


def test_calculate_saturdays_2023_jan():
    # calculate_saturdays関数のテスト
    year = 2023
    month = 1  # 例えば2023年1月
    first_saturday, third_saturday = calculate_saturdays(year, month)
    assert first_saturday == datetime(2023, 1, 7)  # 2023年1月の第一土曜日
    assert third_saturday == datetime(2023, 1, 21)  # 2023年1月の第三土曜日


def test_not_calculate_saturdays_2023_jan():
    # calculate_saturdays関数のテスト
    year = 2023
    month = 1  # 例えば2023年1月
    first_saturday, third_saturday = calculate_saturdays(year, month)
    assert first_saturday != datetime(2023, 1, 6)  # 2023年1月の第一土曜日の一日前
    assert third_saturday != datetime(2023, 1, 20)  # 2023年1月の第三土曜日の一日前
    assert first_saturday != datetime(2023, 1, 8)  # 2023年1月の第一土曜日の一日後
    assert third_saturday != datetime(2023, 1, 22)  # 2023年1月の第三土曜日の一日後


@patch("requests.post")
def test_set_slack_reminder(mock_post):
    # set_slack_reminder関数のテスト
    date = "2023-01-07T09:00:00Z"  # ISOフォーマットの日付
    message = "テストリマインダー"
    user_id = "Rm123"
    mock_post.return_value.json.return_value = {
        "ok": True,
        "reminder": {"id": user_id},
    }  # noqa

    response = set_slack_reminder(date, message)
    print(response)
    mock_post.assert_called_once()
    assert response["ok"]
    assert "reminder" in response
    assert response["reminder"]["id"] == user_id
