import datetime
import time
import pytz

print("Current Epoch time\t", time.time(), "Seconds")
print("Current Epoch time\t", time.time_ns(), "Nanoseconds")

utc_dt = datetime.datetime(2021, 10, 4, 12, 44, 56, 10, tzinfo=pytz.utc)
print("Time Zone aware date time\t", utc_dt)

current_utc_dt = datetime.datetime.now(tz=pytz.utc)
print("Current UTC Time Zone\t", current_utc_dt)

current_utc_dt = datetime.datetime.now(tz=pytz.utc)
print("Convert UTC to India Time zone \t", current_utc_dt.astimezone(tz=pytz.timezone("Asia/Calcutta")))

curr_dt = datetime.datetime.today()
print("Naive time to timezone aware \t", curr_dt, pytz.timezone("Asia/Calcutta").localize(curr_dt))
print("ISO format \t", curr_dt.isoformat())


