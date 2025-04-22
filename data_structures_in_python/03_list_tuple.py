# #ref: https://docs.python.org/3/tutorial/introduction.html#lists
# #ref: https://docs.python.org/3/tutorial/datastructures.html#more-on-lists

numlist = [0,1,2,4,3,5,6]
mixedlist = [1,"two",3.0,3.0,3.0]

# print(numlist)
# print(mixedlist)

# #Like strings (and all other built-in sequence types), lists can be indexed and sliced:
# print(numlist[1:4])

# #You can also add new items at the end of the list, by using the append() method
# numlist.append(9)
# print(numlist)

# numlist = numlist + [9,10]
# print(numlist)

# #lists can be nested:
# nestedlist = [1,"two",3.0,[4,5,"six"]]

# #accessing nested list elements:
# print(nestedlist[3][1])

# #removing elements from a list:  It raises a ValueError if there is no such item.
# mixedlist.remove("two")
# print(mixedlist)
# mixedlist.remove(4)

# #find the position of a element:
# print(mixedlist.index(3.0))

# #sorting a list:
# numlist.sort()
# print(numlist)

# sortedlist = sorted(numlist)
# print(sortedlist)
# print(numlist)

#Joining the elements in a list:
# textlist = ['s','o','n','u']
# joined = "".join(textlist)
# print(joined)

# joinedusingseparator = "-".join(textlist)
# print(joinedusingseparator)

# #splitting a text into a list:
# #Although this is hardly needed as str is itself implemented like a list
# splitlist = list(joined)
# print(splitlist)

# #splitting a text per a separator:
# csvtext = "50,100,200,4000,adani green,BSE"
# adanigreendata = csvtext.split(",")
# print(adanigreendata)

# #copying a list:
# #do not do:
# copiedlist = numlist
# print(numlist)
# print(copiedlist)

# copiedlist.remove(4)

# print(numlist)
# print(copiedlist)

# any changes made to copied list will reflect in original list as it is a mutable datastructure

#instead use:
# copiedlist = numlist.copy()
# print(numlist)
# print(copiedlist)

# copiedlist.remove(4)

# print(numlist)
# print(copiedlist)

# '''--------------------------------------------------------------'''
# #Tuples:
# mytuple = (1,2,3,4,5)
# anothertuple = (1,)

# # '''Tuples are immutable data types
# # So append doesnot apply to it
# # instead you need to do this:'''
# print(anothertuple)
# anothertuple = anothertuple + (2,)
# print(anothertuple)

# #if you need to remove an element:
# position = mytuple.index(4)
# mytuple = mytuple[:position] + mytuple[position+1:]
# print(mytuple)

# # any changes made to copied tuple will not reflect in original tuple as is a mutable datastructure
# #So this works:
# copiedtuple = mytuple
# mytuple = mytuple + (6,)
# print(mytuple)
# print(copiedtuple)

# '''-------------------------------------------------------------'''
# #How to iterate over lists and tuples:

# for i in numlist:
# 	print(i)

# #To get the position as well:
# for pos,val in enumerate(numlist):
# 	print(f"postion: {pos}, value: {val}")

# #Note: Avoid changing the contents of a mutable structure while inside a loop