import time
import numpy as np 
import matplotlib.pyplot as plt 
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0,len(arr)-i-1):
            if arr[i]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
  
times=time.time()
arr=list()
numtimes=list()
for i in range(1,8):
    start=time.time()
    n=int(input("Enter the no of elements:"))
    numtimes.append(n)
    for x in range(n):
        number=np.random.randint(10,99)
        arr.append(number)
    print("list before searching",x+1,"elements")
    print(arr)
    bubble_sort(arr)
    end=time.time()
   
   
    print("list after bubblesorting for",x+1,"elements is")
    print(arr)
    print("time taken for bubblesorting for",n,"elemets is",end-start )
print(numtimes)
print(times)

plt.plot(numtimes,times,label=" bubblesort")
plt.grid()
plt.legend() 
plt.show()