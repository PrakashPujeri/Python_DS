import random
def partition(arr,i,j):
    pivot=arr[i]
    left=i+1
    right=j
    while True:
        while left<= right and arr[left]<pivot:
            left=left+1
        while left<=right and arr[right]>=pivot:
            right=right-1
            if left<right:
                arr[left],arr[right]=arr[right],arr[left]
            else:
                break
    arr[i],arr[right]=arr[right],arr[i]
    return right
def quicksort(arr,i,j):
    if i>=j:
        return
    else:
        pos=partition(arr,i,j)
        quicksort(arr,i,pos-1)
        quicksort(arr,pos+1,j)
#main code    
n=int(input("enter the elements:"))
arr=[]
for i in range(n):
    num=random.randint(1,99)
    arr.append(num)
print("list before sorting")
print(arr)
quicksort(arr,0,len(arr)-1)
print("sorted list is :",arr)


    