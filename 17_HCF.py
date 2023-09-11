# Print HCF number (Highest Common Factor)
num1=int(input("Enter num1: "))
num2=int(input("Enter num2: "))
HCF=1
for i in range(1, min(num1, num2)):

    if num1 % i == 0 and num2 % i == 0:
        HCF = i

print("HCF is : ",HCF)