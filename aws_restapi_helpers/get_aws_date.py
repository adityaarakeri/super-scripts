import datetime

t = datetime.datetime.utcnow()
amzdate = t.strftime('%Y%m%dT%H%M%SZ')

print(amzdate)