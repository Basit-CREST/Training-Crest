import time,pendulum



def timmer(end):
    
    remainig_time = end.diff(pendulum.now())
    while remainig_time.total_seconds() > 1:
        print("Remaining Time " + str(remainig_time.total_seconds()))
        time.sleep(1)
        currrent_time = pendulum.now()
        remainig_time = end.diff(currrent_time)




print("Greetings\n" + str(pendulum.now()))
currrent = pendulum.now()
end_time = currrent.add(minutes=1)
timmer(end_time)
print("Boom!!!!")
