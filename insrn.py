def insertionsort(arr):
    for i in range(1,len(arr)):
       key=arr[i]
       j=i-1
       while j>=0 and key<arr[j]:
           arr[j+1]=arr[j]
           j=j-1
       arr[j+1]=key
arr=[1,67,91,356,8,9,67,4]
insertionsort(arr)
print(arr)