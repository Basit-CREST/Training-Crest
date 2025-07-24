import datetime as dt
from datetime import time , timedelta


print("Today's Date: " + str(dt.datetime.today()))

t = dt.datetime.today() - timedelta(5)

print("Before 5 days " + str(t))