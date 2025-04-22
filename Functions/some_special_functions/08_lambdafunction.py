# lambda:
# Python code to illustrate cube of a number
# showing difference between def() and lambda().
def cube(y):
    return y*y*y

g = lambda y: y*y*y
print(g(7))

print(cube(5))

#----------------------------------------------------------------

def make_incrementor(n):
    return lambda x: x + n
    # def adder(x):
    #     return x+n
    # return adder

adder = make_incrementor(42)
print(adder(0))
print(adder(1))
