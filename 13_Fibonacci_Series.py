# print the  Fibonacci Series in python ( 0 1 1 2 3 5 8 13 21 34 )
num=int(input("Enter the number : "))
a = 0
b = 1
sum = a+b
count = 1
while (count <= num):
    count += 1
    print(a, end=" ")
    a = b
    b = sum
    sum = a + b


