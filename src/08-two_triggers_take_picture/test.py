import datetime, time

a = datetime.datetime.now()
print(a)
time.sleep(0.5)
b = datetime.datetime.now()
print(b)
print((b-a).total_seconds() < 0.51)