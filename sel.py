def sel(a):
      
    for i in range(len(a)):
        for j in range(i,len(a)):
               if a[i] >a[j]:
                   a[j],a[i]=a[i],a[j]
a= [10,4,5,16,9,21] 
sel(a)                       
print(a) 