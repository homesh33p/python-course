# a=1
# b=2
# c=a+b
# print(c)

# mydecimal = 1.1
# print(type(mydecimal))

# # print(type(a))

# # c = a + mydecimal
# # print(type(c))

# # MyDecimal = 2

# print(mydecimal)
# print(MyDecimal)

# print(1)
# choice = "y"
# mylist = []
# while choice !='':
#     choice = input()
#     print(choice)    
#     if choice:
#         mylist.append(choice)



# choice = "y"
# mylist = []
# while bool(choice):
#     choice = input("enter the value")
#     mylist.append(choice)

for i in [1,2,3,4,5]:
	if i == 1:
		print("one")
	elif i == 2:
		choice = int(input())
		if choice == 1:
			print("user input: %d"%(choice))
		else:
			break
	else:
		print('greater than 2')


