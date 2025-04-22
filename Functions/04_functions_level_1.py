#ref: https://docs.python.org/3/tutorial/controlflow.html#defining-functions
import types

# defining a function

# def square(num):
#     return num**2

# #calling a function:
# squareofnum = square(2)
# print(squareofnum)

# # functions my not have any return statement
# # in such a case the default return value is None
# def square(num):
#     print(f"square of {num} is {num**2}")

# # squareofnum = square(2)
# # print(squareofnum)

# # #functions may not accept any arguments as well:
# # def square():
# #     a = 2
# #     print(f"square of {a} is {a**2}")

# # square()

# #functions are objects, just like variables, except they are callable

# def fib(n):
#     """Print a Fibonacci series up to n."""
#     a, b = 0, 1
#     fib = []
#     while a < n:
#         fib.append(a)
#         # c = b
#         # b = a+b
#         # a = c
#         a, b = b, a+b
#     fib = (str(i) for i in fib) #convert to string so that we can use join function
#     print(" ".join(fib))

# #this will return a function object
# # print(fib)
# # # print(type(fib))
# # # #this will return the memory location of the function object
# # # print(id(fib))
# # fib(50)

# #this means that a function can be passed around like a variable, but be careful not to call the function
# def acceptafunc(anotherfunc,num):
#     print(f"starting {anotherfunc.__name__}")
#     anotherfunc(num)
#     print(f"ending {anotherfunc.__name__}")

# num = 50
# # acceptafunc(fib,num)

# #it can also be stored as a variable:
# mychoice = {1:square,2:fib}

# print(mychoice[1])
# print(mychoice[2])

# mychoice[1](3)

# choice = 'dummy val'
# while choice in [1,2,'dummy val']:
#     #if the user input is a integer, then proceed or break from the loop
#     if choice !="dummy val":
#         userinputnum = int(input("Number: "))
#         mychoice[choice](userinputnum)

#     print("1: to print square of a num\n2: print Fibonacci till the num")
#     choice = input("Your choice")
#     if choice.isdigit():        
#         choice = int(choice)
# check if an object is callable:

# print(callable(fib))
# if isinstance(fib,types.FunctionType):    
#   print("function")
# else:
#   print("not")

# you can have multiple return statements in a function:
# def userinput(num):
#     if num.lower() == "one":
#         return 1
#     elif num.lower() == "two":
#         return 2
#     elif num.lower() == "three":
#         return 3
#     else:
#         return "beyond 3"

# output = userinput("Two")
# print(output)
# print("ayayayay")

# a more practical example of usage if multiple return statements is as follows:

def divide(num1,num2):
    if not type(num1) in [float,int]:
        print("Incorrect arguments passed")
        return
    if not type(num2) in [float,int]:
        print("Incorrect arguments passed")
        return    
    if not num2:
        print("Divisor cannot be zero")
        return
    print(f"{num1}/{num2} = {num1/num2}")
    return num1/num2

a = [2,6,4,"8"]
b = [1,0,2]

for num1 in a:
    for num2 in b:
        result = divide(num1,num2)
        print(f"result: {result}")

# a function can return multiple values at the same time:
def squareandcube(num):
    return num**2,num**3

sq,cube = squareandcube(2)
print(sq)
print(cube)

returnval = squareandcube(2)
print(returnval)
