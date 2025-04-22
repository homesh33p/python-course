# # words = ['cat', 'window', 'defenestrate']
# # for w in words:
# #   print(w, len(w))

# mylist = list(range(6)) 
# print(mylist)

# #The range() Function
# for i in range(5):
#   print(i)

# # #The given end point is never part of the generated sequence;
# # #  range(10) generates 10 values

# # #while loop:
# print("have you stopped beating your wife?")
# choice = input("Enter y/n")
# while choice.lower() not in ["y","n"]:
#     choice = input("Enter y/n")

# # syntax
# while (condition):
#   do something

# Another example of printing 10 numbers, in steps of 2, starting from user input number:
# userinputnum = int(input("Enter a number"))
# counter = 1
# while counter<11:
#   print(userinputnum)
#   userinputnum+=2 # the operator += means short for: ex: i = i+1 --> i+=1
#   counter+=1

# #example of infinite loop:
# while True:
#     pass

#loops can be nested:
# print(list(range(3)))
# for i in range(0,6,2):
#   for j in range(3):
#       print(("a"*i)+("*"*j))

# #break and continue Statements, and else Clauses on Loops


# #break:
# #example: if the user enters y then continue else break from the loop
# choice = "y"
# while True:
#   choice = input("continue?")
#   if choice.lower()=="y":
#       continue
#   else:
#       break

# #example : checking if prime (use of else in loops)
# n = int(input("input a integer between 2,100"))
n = 15
for x in [2,3,5,7]:
    if n % x == 0:
        print(f"{n} divisible by {x}")
        break
else:
# loop fell through without finding a factor
    print(n, 'is a prime number')