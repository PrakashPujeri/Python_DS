def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
num=int(input("enter the number:"))
print(num, "this number factorial number is:",fact(10))