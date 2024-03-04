a= [10,4,5,16,9,21]
for i in range(len(a)):
        for j in range(0,len(a)-i-1):
            if a[j]> a[j+1]:
                   a[j],a[j+1]=a[j+1],a[j]
print(a)
