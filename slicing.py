# index values slicing

fruits =['Apple','Mango','Banana','Cherry','Orange','watermelon','chickoo','grapes']
print(fruits)              # Output  : ['Apple', 'Mango', 'Banana', 'Cherry', 'Orange', 'watermelon', 'chickoo', 'grapes']
print(fruits[0])           # Output  : Apple
print(fruits[1:])          # Output  : ['Mango', 'Banana', 'Cherry', 'Orange', 'watermelon', 'chickoo', 'grapes']
print(fruits[:5])          # Output  : ['Apple', 'Mango', 'Banana', 'Cherry', 'Orange']
print(fruits[1:3])         # Output  : ['Mango', 'Banana']
print(fruits[-1])          # Output  : grapes
print(fruits[-5:-1])       # Output  : ['Cherry', 'Orange', 'watermelon', 'chickoo']
print((fruits[:]))         # Output  : ['Apple', 'Mango', 'Banana', 'Cherry', 'Orange', 'watermelon', 'chickoo', 'grapes']