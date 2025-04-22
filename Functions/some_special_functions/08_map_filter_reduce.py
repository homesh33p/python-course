#map,filter,reduce

# Python code to illustrate
# filter() with lambda()
# li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
#syntax:
#filter(funct,iterable)
# def func(x):
# 	return x%2 != 0
#
# final_list = list(filter(lambda x: (x%2 != 0) , li))
# print(final_list)

#-----------------------------------------------------------------------

# Python code to illustrate
# map() with lambda()
# to get double of a list.
# li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
# final_list = list(map(lambda x: x*2 , li))
# print(final_list)

#----------------------------------------------------------------------

# Python code to illustrate
# reduce() with lambda()
# to get sum of a list
from functools import reduce
li = [5, 8, 10, 20, 50, 100]
sum = reduce((lambda x, y: x + y), range(100))
print (sum)