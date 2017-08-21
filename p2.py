import time


print(time.time(), time.ctime())

count0 = 100
while count0 > 0 :

    count0-= 1
    print(time.ctime(), count0)
    time.sleep(2)

print('go home')

