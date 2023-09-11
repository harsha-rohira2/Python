# Print LCM (Least common Multiple)
num1=int(input("Enter num1: "))
num2=int(input("Enter num2: "))
HCF=1
for i in range(1,max(num1,num2)):
    if num1 % i == num2 % i ==0:
        HCF=i

LCM=(num1 * num2)
print("LCM is : ",LCM)