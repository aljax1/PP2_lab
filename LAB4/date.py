#1
from datetime import date,  timedelta, datetime

current = date.today() - timedelta(5)

print("Current time: ", date.today())
print("Substact five days: ",current)


#2
from datetime import date,  timedelta, datetime

time = datetime.now() - timedelta(1)
yesterday = time.strftime("%d-%m-%Y")
print("Yesterday: ",yesterday)

time = datetime.now()
today = time.strftime("%d-%m-%Y")
print("Today: ",today)

time = datetime.now() + timedelta(1)
tomorrow = time.strftime("%d-%m-%Y")
print("Tomorrow: ", tomorrow)



#3
from datetime import date,timedelta,datetime

time = datetime.now()
withoutmicroseconds = time.strftime("%d-%m-%Y, %H:%M:%S")

print(withoutmicroseconds)



#4
from datetime import datetime, timedelta

now = datetime.now()
yesterday = now - timedelta(days=1)
tomorrow = now + timedelta(days=1)

yesterday_timestamp = yesterday.timestamp()
tomorrow_timestamp = tomorrow.timestamp()

print(tomorrow_timestamp - yesterday_timestamp)