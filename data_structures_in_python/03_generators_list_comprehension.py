#ref: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions

#List comprehension:

squaresfromloop = []
for i in range(500000):
	sq = i**2
	squaresfromloop.append(sq)

# print(squaresfromloop)
# squaresfromloop.clear()

# #or use one line for loops:
# squaresfromloop = [i**2 for i in range(5)]
# print(type(squaresfromloop))
# print(squaresfromloop)

# #We can have if statement in them as well:
# evennumbers = [num for num in range(11) if num%2==0]
# print(evennumbers)
# #This is equivalent to:
# evennumbers.clear()
# for num in range(11):
# 	if num%2==0:
# 		evennumbers.append(num)
# print(evennumbers)


# '''----------------------------------------------------------------------'''
# #Generators/iterators
# #ref: https://docs.python.org/3/glossary.html#term-iterable
squaregen = (i**2 for i in range(5))
print(type(squaregen))
print(squaregen)

# # listSquaregen = list(squaregen)
# # print(type(listSquaregen))
# # print(listSquaregen)

# #Once the generator object has been utilised, its empty
# listSquaregen2 = list(squaregen)
# print(squaregen)
# print(listSquaregen2)
# print(list(squaregen))

print(type(range(5)))

#range() function is in fact a generator

'''
Generators generate/calculate the value on the spot and return the value
They donot store the value once it has been supplied
They are much faster in calculations involving series of number/float/any data type
They are much lighter on the memory of the computer and are less resource hungry

Note: Never compare a generator to a list or tuples
They are not a data structure in any way, they donot hold any data within them, unlike list/tuple
They are objects that return a stream of data, elements of which are calculated on the spot
They are infact functions
More on how to create custom generators in the functions section
'''



