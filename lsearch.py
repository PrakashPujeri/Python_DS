import time
import random
lists=[]
def bigglist(num):
    for i in range(num):
        lists.append(random.randint(1,99))
    lists.append(89)

bigglist(1000)
print(lists)

def linearsearch(arr,x):
    for i in range(len(arr)):
        if (arr[i]==x):
            return i
        
    return-1

x=78
start_time=time.time()
value=linearsearch(lists,x)
end_time=time.time()
print(value,"end and start time =",end_time-start_time)