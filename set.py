""" 1. List are UnOrdered, It is  UnChangeable, It No Duplicates Allowed
    2. List usr Curly Brackets { }
"""
myset = {"C","CPP","JAVA","PYTHON","AWS","HTML"}
set ={"CSS","ANDROID","C","IOT"}

print(myset)            # print set
# Output  {'PYTHON', 'CPP', 'AWS', 'JAVA', 'C', 'HTML'}

print(len(myset))       # print length of set
# output  6

print(type(myset))      # print type
# Output  <class 'set'>

myset.add("PHP")        # Add item in set
print(myset)
# output  {'PHP', 'JAVA', 'C', 'PYTHON', 'HTML', 'CPP', 'AWS'}

myset.update(set)          # update the set
print(myset)
# output   {'PHP', 'HTML', 'IOT', 'CPP', 'PYTHON', 'JAVA', 'AWS', 'CSS', 'C', 'ANDROID'}

myset.union(set)          # union method the set
print(myset)
# output    {'PHP', 'HTML', 'IOT', 'CPP', 'PYTHON', 'JAVA', 'AWS', 'CSS', 'C', 'ANDROID'}

y = myset.intersection(set)          # intersection the set
print(y)
# output  {'C', 'CSS', 'ANDROID', 'IOT'}

myset.intersection_update(set)          # intersection update the set
print(myset)
# output  {'C', 'CSS', 'ANDROID', 'IOT'}

myset.difference(set)          # difference the set
print(myset)
# output  {'CSS', 'ANDROID', 'C', 'IOT'}

myset.symmetric_difference_update(set)          # symmertic difference update the set
print(myset)
# output set()







