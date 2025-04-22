#ref: https://docs.python.org/3/library/stdtypes.html#string-methods

'''Write a Python program to print the following string in a specific format :
Twinkle, twinkle, little star,
	How I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky. 
Twinkle, twinkle, little star, 
	How I wonder what you are
'''
# print("""Twinkle, twinkle, little star,
# 	How I wonder what you are! 
# 		Up above the world so high,   		
# 		Like a diamond in the sky. 
# Twinkle, twinkle, little star, 
# 	How I wonder what you are""")

#Write a Python program which accepts the radius of a circle from the user and compute the area

# r=int(input("enter the radius of circle"))
# pi=3.14
# area=pi*(r)**2
# print(area)


#Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them
# a=input("enter your first name")
# b=input("enter your last name")
# c=b+a
# print(c)
'''
Find the position of "." in the user input string
'''
# a=input("user input")
# a.find(".")
# b=(a.find("."))
# print(b)
'''
Write a Python program to accept a filename from the user and print the extension of that
Sample filename : abc.java
Output : java
'''

'''
Write a Python program to get a new string from a given string where "--" has been added to the front and back
eg: input: "--stupid--"
output: "stupid"
'''

# a = input()
# b = a.replace("-","")
# print(b)

'''
Write a Python program to get a string which is n (non-negative integer) copies of a given string
Sample string: "abc"
n (input): 5
output: "abcabcabcabcabc"
'''


'''
Check if a string is palindrome:
eg: "ICICI"
Reverse is also "ICICI"
So its a palindrome
'''


'''
Check if a number is palindrome
'''

'''
Check if a given character is duplicate in the string: "abracadabra"
eg: input: "b"
Output: "occurs 2 times"
input: "c":
Output: "Occurs 1 times"
'''
# a=input("anything")
# a.count("b")
# b=(a.count("b"))
# a.count("c")
# d=(a.count("c"))
# print(b)
# print(d)
'''
Check if a input file name is a zip file or not:
eg:
input: "transactions.txt"
output: "No"
input: "semester admit cards.zip"
output: "Yes"
'''
# a=input("enter file name ")
# pos=a.find(".")
# pos=pos+1
# ext=a[pos:]
# print(ext)


'''
Check if a string is alphanumeric
alphanumeric string doenot contain any special character
eg: jeffbesos@amazon.com
output: False

input: jeffbesosamazoncom
output: True
'''

'''
Replace with "@" the fist occurence of a character from the right side in the string: Vitalik Buterin

input: "a"
output: Vit@lik Buterin
'''

'''
Check if a string can be converted to an integer:
eg input: "C3PO"
output: False

input: "98249"
output: True

'''

# a = 3
# b=4

# if (a>b):
# 	print("a is greater than b")
# else:
# 	print("a is less than b")