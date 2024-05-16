def binarysearch(arr,x):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]<x:
            low=mid+1
        else:
            high=mid-1
    return -1
arr=[5,7,15,25,687,1000]
x=int(input("enter your search number:"))
result=binarysearch(arr,x)
if result!=-1:
    print(result)
else:
    print("not present")