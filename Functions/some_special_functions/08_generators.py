'''
----------------------------------------------------------------
    # Generators:
    #     refer: https://realpython.com/introduction-to-python-generators/

----------------------------------------------------------------	
'''
# a = list(range(100))
# nums_squared_gc = (num**2 for num in range(5))
# print(type(nums_squared_gc))
# print(next(nums_squared_gc))
# print(next(nums_squared_gc))

#cannot generate infinte sequence with a range or function
#We can do that using generators
# generators use the "yield" keyword

def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1
#
gen = infinite_sequence()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

'''
Generator functions look and act just like regular functions,
but with one defining characteristic.
Generator functions use the Python yield keyword 
instead of return. 

When the Python yield statement is hit, 
the program suspends function execution and
returns the yielded value to the caller. 

(In contrast, return stops function execution completely.)
 
When a function is suspended,
the state of that function is saved.
This includes any variable bindings local to the generator,
the instruction pointer, the internal stack,
 and any exception handling.
 
Then the function is resumed when you call next() in the function
'''