def binarySearch(arr,target):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return -1
arr=[1,2,5,6,8,9,20]
target=20
result=binarySearch(arr,target)
if result!= -1:
    print("element is present in the index:",result)
else:
    print("element is not present in the index")