import datetime

#UTC
TheStart = datetime.date(2024,12,31) #1 day before
Now = datetime.date.today()

print(Now - TheStart)