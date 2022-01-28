from email.utils import localtime
import time;

initial = time.time();
print('initial', initial)

for i in range(45):
    print('sam')
    time.sleep(2)

forloop = time.time()
print('forloop', forloop-initial)

k=0
while(k<45):
    print('sam')
    k+=1

whileloop = time.time()
print('whileloop', whileloop-forloop)

#-----------------------------------------------------------------------

localTime = time.asctime(time.localtime(time.time())) #.localtime() returns a tuple of local time
print(localTime);