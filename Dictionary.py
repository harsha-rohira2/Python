""" 1. Dictionary are Ordered, It is Changeable, It do not allow Duplicates
    2. List usr Curly Brackets { }
    3. It store value in Key:value
"""

mydict = {
    "name" : "Harsha",
    "gender" : "Female",
    "age" : 23
}
print(mydict)           # print dictionary
# Output  {'name': 'Harsha', 'gender': 'Female', 'age': 23}

print(type(mydict))     # print type od dictionary
# Output  <class 'dict'>

print(mydict["age"])       # print age
# Output  23

print(mydict.get("gender"))
# output  Female

print(len(mydict))      # length of Dictionary
# output  3

"""  Key Method  """
x = mydict.keys()
print(x)                 # before change
# Output  dict_keys(['name', 'gender', 'age'])
mydict["color"] = "fair"
print(x)                 # after change
# output   dict_keys(['name', 'gender', 'age', 'color'])

"""  Values Method  """
x = mydict.values()
print(x)            # before change
# Output  dict_values(['Harsha', 'Female', 23, 'fair'])
mydict["color"] = "fair"
print(x)                 # after change
# output  dict_values(['Harsha', 'Female', 23, 'fair'])

"""  Copy  """
x = mydict.copy()
print(x)
# output  {'name': 'Harsha', 'gender': 'Female', 'age': 23, 'color': 'fair'}

""" clear """
x = mydict.clear()
print(x)
# output  None

