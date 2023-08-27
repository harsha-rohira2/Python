""" 1. List is use store multiple Iem in single Variable
    2. List are Ordered, It allowed Changes, It allowed Duplicates
    3. List usr Square Brackets [ ]"""

mylist = [23,45,'Apple','Grapes',76.08,"Sunday",10,'Grapes']

print(mylist)           # print List
# Output  [23, 45, 'Apple', 'Grapes', 'Sunday', 67.54, 10,, 'Grapes']

mylist[0] = 50          # Replace 0 index value by 50
print(mylist)
# output [50, 45, 'Apple', 'Grapes', 76.08, 'Sunday',10, 'Grapes']

mylist.insert(2,'Orange')
print(mylist)           # insert new value at 2 position
# output [50, 45, 'Orange', 'Apple', 'Grapes', 76.08, 'Sunday', 10,  'Grapes']

mylist.append("Mango")
print(mylist)           # append add new value at the end of list
# output [50, 45, 'Orange', 'Apple', 'Grapes', 76.08, 'Sunday', 10, 'Grapes', 'Mango']

print(len(mylist))      # length of list
# output 12

mylist.remove(10)       # remove
print(mylist)
# output  [50, 45, 'Orange', 'Apple', 'Grapes', 76.08, 'Sunday', 'Grapes', 'Mango']

mylist.pop()            # it will remove from the end of list
print(mylist)
# output [50, 45, 'Orange', 'Apple', 'Grapes', 76.08, 'Sunday', 'Grapes']

mylist.pop(5)           # it will remove from index value ie. 5 ie. 76.08
print(mylist)
# output [50, 45, 'Orange', 'Apple', 'Grapes', 'Sunday', 'Grapes']

mylist.pop(0)
print(mylist)
# output [45, 'Orange', 'Apple', 'Grapes', 'Sunday', 'Grapes']

del mylist[0]           # it will delete the index podition
print(mylist)
# output ['Orange', 'Apple', 'Grapes', 'Sunday', 'Grapes']

mylist.sort()           # Sort in alphabate order
print(mylist)           # ***NOTE: It will take only Aphabate or Number is List No Mixture of alphabate and numbers***
# Output  ['Apple', 'Grapes', 'Grapes', 'Orange', 'Sunday']

mylist.sort(reverse = True)         # Sort in alphabate descending order
print(mylist)           # ***NOTE: It will take only Aphabate or Number is List No Mixture of alphabate and numbers***
# output  ['Sunday', 'Orange', 'Grapes', 'Grapes', 'Apple']

mylist.reverse()                    # reverse order of list
print(mylist)
# output ['Apple', 'Grapes', 'Grapes', 'Orange', 'Sunday']

mylist.clear()              # it will clear the list and output will be empty list
print(mylist)
# output []

del mylist                  # It will delete the list no output
print(mylist)








