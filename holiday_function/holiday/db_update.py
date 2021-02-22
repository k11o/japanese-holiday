from urllib import request
import csv
import datetime

HOLIDAY_CSV_URL = "https://www8.cao.go.jp/chosei/shukujitsu/syukujitsu.csv"
LOCAL_PATH = "/tmp/syukujitsu.csv"


def lambda_handler(event, context):
    request.urlretrieve(HOLIDAY_CSV_URL, LOCAL_PATH)
    reader = csv.reader(open(LOCAL_PATH, newline='', encoding='cp932'))
    for [date_str, name] in reader:
        try:
            holiday = datetime.datetime.strptime(date_str, '%Y/%m/%d').date()
            print(holiday)
        except ValueError:
            # 日付が入ってない行は読み飛ばす
            pass
    return ""
