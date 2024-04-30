def linearsearch (arr,x):
    i=0
    while i<len(arr):
         if arr[i]==x:
            return i
         i=i+1
    return-1
arr=[54,52,4,87,4,8]
x=4

print(linearsearch(arr,x))

