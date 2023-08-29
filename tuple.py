""" 1. List are Ordered, It is  UnChangeable, It allowed Duplicates
    2. List usr Round Brackets ( )
"""
mytuple = ("Mumbai","Pune","Nashik","Banglore","Delhi")

print(mytuple)              # print tuple
# Output   ('Mumbai', 'Pune', 'Nashik', 'Banglore', 'Delhi')

print(len(mytuple))         # length of Tuple
# Oitput  5

print(type(mytuple))        # type of tuple
# Output  <class 'tuple'>

y = list(mytuple)           # convert tuple into list
print(y)
# Output  ['Mumbai', 'Pune', 'Nashik', 'Banglore', 'Delhi']

y=("Hyderbad",)             # add tuple to a tuple
mytuple += y
print(mytuple)
# Output  ('Mumbai', 'Pune', 'Nashik', 'Banglore', 'Delhi', 'Hyderbad')

"""If we need to change the tuple we need to convert to list and change it """

newtuple = list(mytuple)               # change value by using index number
newtuple[1] = "Surat"
mytuple = tuple(newtuple)
print(mytuple)
# Output  ('Mumbai', 'Surat', 'Nashik', 'Banglore', 'Delhi', 'Hyderbad')

newtuple = list(mytuple)               # insert value to tuple using index position
newtuple.insert(2,"Chennai")
mytuple = tuple(newtuple)
print(mytuple)
# Output  ('Mumbai', 'Surat', 'Chennai', 'Nashik', 'Banglore', 'Delhi', 'Hyderbad')

newtuple = list(mytuple)               # remove vale from tuple
newtuple.remove("Nashik")
mytuple = tuple(newtuple)
print(mytuple)
# Output  ('Mumbai', 'Surat', 'Chennai', 'Banglore', 'Delhi', 'Hyderbad')


""" Unpacked Tuple = Extract value back into variable is called unpacked tuple"""
fruits = ("Apple","Mango","Orange")
(a1,a2,a3) = fruits
print(a1,a2,a3)
# outout      Apple Mango Orange

(a1,a2,*a3) = fruits
print(a1,a2,a3)
# output      Apple Mango ['Orange']

