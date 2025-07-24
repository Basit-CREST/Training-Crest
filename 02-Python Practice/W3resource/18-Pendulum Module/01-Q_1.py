import pendulum
import re
now = pendulum.now()
print(now)
print(now.add(months=1))
print(now.format("YY"))  ## YY-MM
print(type(now.format("YY")))
print(pendulum.now('Europe/Dublin'))
print(pendulum.now('Europe/Madrid'))
universal = pendulum.now('UTC')

#print(pendulum.timezones())
tz = pendulum.timezones()
print(type(tz))

ans = [ i for i in tz if re.findall(r'^Indian/',i)]
print(ans)


print(universal.in_tz('Indian/Cocos'))