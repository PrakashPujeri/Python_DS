def fib(n):
    if n<=0:
        return 1
    else:
        return fib(n-1)+fib(n-2)
target=int(input("enter the number:"))
for i in range (target):
    print(i,end=" ")