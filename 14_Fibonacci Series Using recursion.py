# print the  Fibonacci Series using Recursion in python ( 0 1 1 2 3 5 8 13 21 34 )

def fibonacci_series(i):
    if i<=1:
        return i
    else:
        return fibonacci_series(i-1)+fibonacci_series(i-2)

num=int(input("Enter num: "))
if num<=0:
    print("Enter positive number")
else:
    print("Fibonacci series",end=" ")
    for i in range(num):
        print(fibonacci_series(i),end=" ")