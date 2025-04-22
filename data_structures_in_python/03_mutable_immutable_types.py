# Immutable types: int,str,float,tuple
# Mutable types: dict,list

# A immutable type is never altered at the memory location

a = 1
print(id(a))

b = a
print(id(b))

b+=1
print(b)
print(id(b))

# A mutable type is changed in the memory location:

a = [1,2,3,4]
print(id(a))
a.append(5)
print(id(a))

b = a
# any change made to b, will also reflect on a , as a is pointing to the same memory location
b.append(6)
print(f"id: {id(a)}, value: {a}")
print(f"id: {id(b)}, value: {b}")

# this is why list and tuples are inherently different
# This is also the reason why we cant append to a tuple, we need to always create a new tuple:
b = b +(7,)
a = (1,2,3,4)
print(id(a))
a = a + (5,)
print(id(a))

b = a
# any change made to b, will not reflect on a , as a and b are pointing to the different memory locations
b = b + (6,)
print(f"id: {id(a)}, value: {a}")
print(f"id: {id(b)}, value: {b}")

