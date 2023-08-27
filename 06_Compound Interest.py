principle = float(input("Enter the Principle Amount: "))
rate = float(input("Enter the Rate: "))
time= int(input("Enter the time: "))
CI = principle * (pow((1+rate/100), time))
print("Compound Interst is:",CI)

