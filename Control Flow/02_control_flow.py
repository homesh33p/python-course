# #ref: https://docs.python.org/3/tutorial/controlflow.html

# #General Statement
# if 1>2:
# 	print("One is greater")
# else:
# 	print("Two is greater")

# if bool(1>2)==True:
# 	print("One is greater")
# else:
# 	print("Two is greater")


# #use of elif:
# mynum = int(input("Enter a number "))
# if mynum == 1:
# 	print("One")
# elif mynum == 2:
# 	print("Two")
# elif mynum == 3:
# 	print("Three")
# else:
# 	print("Beyond Three")

#Can you implement the above logic by using dictionary?

#Python doesnot have a switch statement, instead use elif as above

#use of pass statement:
#example: check if a number is divisible by 2 or 3. If divisible by both dont do anything print.
# If divisible by only one of them, print the factor
mynum = 4

if (mynum%2==0 and mynum%3==0):
	pass
elif mynum%2==0:
	print("Divisible by 2 only")
elif mynum%3==0:
	print("Divisible by 3 only")
# else:   #this is not needed, only to show that omitting the else part is equivalent to this statement*/
# 	pass




