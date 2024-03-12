import time
import numpy as np
import matplotlib.pyplot as plt
def insertionsort(arr):
    for i in range(1,len(arr)):
       key=arr[i]
       j=i-1
       while j>=0 and key<arr[j]:
           arr[j+1]=arr[j]
           j=j-1
       arr[j+1]=key

times=list()
arr=list()
numtimes=list()
for i in range (1,8):
    start=time.time()
    n=int(input("enter the no of elements:"))
    numtimes.append(n)
    for x in range (n):
        number=np.random.randint(10,88)
        arr.append(number)
    print("before searching",x+1,"elements")
    print(arr)
    insertionsort(arr)
    end=time.time()
    times.append(end-start)
    print("list after linearsearch of",x+1,"elements")
    print(arr)
    print("time taken for linearch for",n,"elements is",end-start)
    print (numtimes)
    print(times)
           
plt.plot(numtimes,times,label=" insertionsort")
plt.grid()
plt.legend()
plt.show()
    
           
