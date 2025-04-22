#ref: https://docs.python.org/3/library/datetime.html

from datetime import datetime,timedelta
import pytz

ist = pytz.timezone("Asia/Kolkata")
gmt = pytz.timezone("GMT")

nowTimeLocal = datetime.now()
print(nowTimeLocal)
# The above is a timezone unaware time

#belwo is a timezone aware time
nowtimeIst = datetime.now(ist)
print(nowtimeIst)
#
# interpret the datetime in another timezone
# and adds timezone info
asGMT = nowtimeIst.astimezone(gmt)
print(asGMT)

print(type(asGMT))

# #converting datetime objects:
asString = asGMT.strftime("%d %b %y - %H %M %S")
print(asString)
#
#Converting string to datetime object:
asDatetime = datetime.strptime(asString,"%d %b %y - %H %M %S")
print(asDatetime)

#add timezone:
gmtTime = gmt.localize(asDatetime)
print(gmtTime)
print(gmtTime.tzinfo)
#
#Operations with datetime objects:
toadd = timedelta(hours=5)
# toadd = 5
timeafter5hours = gmtTime + toadd
print(timeafter5hours)
#
#difference between two times:
diff = timeafter5hours - gmtTime
print(diff)

