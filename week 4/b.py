from datetime import datetime, timedelta
today = datetime.now().date()
oneday = timedelta(1)
yesterday = today - oneday
tomorrow = today + oneday
print(yesterday, today, tomorrow)