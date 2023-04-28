import datetime


def today_date():
    return datetime.datetime.now()


def today_delta(hours):
    return datetime.datetime.now() - datetime.timedelta(hours=hours)
