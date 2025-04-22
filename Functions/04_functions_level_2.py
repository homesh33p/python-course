# ref: https://docs.python.org/3/tutorial/controlflow.html#default-argument-values
#default argument values in python
# def joinlist(mylist,separator=","):
# 	print(separator.join(mylist))	

# letters = ['s','a','k','e','t']
# # #if no argument is given for the named argument, it will take the default value, else the supplied value
# # joinlist(letters)
# # joinlist(letters,separator="-")

# #this is the same as writing:
# def joinlist(mylist,separator):
# 	if not separator:
# 		separator = ","
# 	print(separator.join(mylist))
# # #but in this case, when calling the function, we need to provide the separator value
# # #we cannot skip the separator argument,else an error will be thrown:

# try:
# 	joinlist(letters)
# except Exception as e:
# 	print(e)

# #it can however be called like this:
# joinlist(letters,separator=None)
# joinlist(letters,separator="")
# joinlist(letters,separator="-")
# joinlist(letters,"-")

# '''Important warning: The default value is evaluated only once.
# This makes a difference when the default is a mutable object such as a list,
# dictionary, or instances of most classes. 
# For example, the following function accumulates the arguments passed to it on subsequent calls:
# '''
# def listify(a, L=[]):
# 	L.append(a)
# 	# L = L +(a,)
# 	return L

# l = ["saket","om"]
# print(listify(1))
# print(listify(2))
# print(listify(3))
# print(l)

# '''If you don’t want the default to be shared between subsequent calls,
# you can write the function like this instead:'''

# def listify(a, L=None):
# 	if L is None:
# 		L = []
# 	L.append(a)
# 	return L

# print(listify(1))
# print(listify(2))
# print(listify(3))

#when a argument is given only as per position, its called positional argument
# joinlist(letters,"-")
# #when a argument is given as keyword/named, its called keyworded argument
# #separator is a keyworded argument below:
# joinlist(letters,separator="-")

# #keyworded arguments cannot be defined or supplied before postional arguments:

#this is wrong:
# def divbytwo(a=2,num):
# 	print(f"{num} divided by {a} : {num/a}")

# #this is correct:
# def divbytwo(num,a=2):
# 	print(f"{num} divided by {a} : {num/a}")

# # divbytwo(num=4)


#------------------------------------------------------------------------------------------------------

#*args,**kwargs

# *args : normal arguments
# def listify(*args):
# 	print(f"arguments: {args}")
# 	mylist = []
# 	for arg in args:
# 		mylist.append(arg)
# 	return mylist

# output = listify(1,2,"om",4.5)
# print(output)

# **kwargs : key worded arguments
# def dictify(**kwargs):
# 	print(f"keyworded arguments: {kwargs}")
# 	print(kwargs.items())
# 	for keyword,argument in kwargs.items():
# 		print(f"keyword: {keyword}, argument: {argument}")
# 		return kwargs

# dictify(learner1="om",learner2="saket",year=2021)


# def pizzashop(kind, *arguments, client = "utso",**keywords):
# 	print("-- Do you have any", kind, "?")
# 	print("-- I'm sorry, we're all out of", kind)
# 	print(client)
# 	for arg in arguments:
# 		print(arg)
# 	print("-" * 40)
# 	for kw in keywords:
# 		print(kw, ":", keywords[kw])

# # It could be called like this:

# pizzashop("pizza", "pizza hut is better than dominoes",
# 	   "mojo pizza is the best",
# 	   shopkeeper="Michael Palin",
# 	   client="John Cleese",
# 	   sketch="Pizza Sketch")

'''Output:
-- Do you have any pizza ?
-- I'm sorry, we're all out of pizza
pizza hut is better than dominoes
mojo pizza is the best
----------------------------------------
shopkeeper : Michael Palin
client : John Cleese
sketch : Pizza Sketch
'''

# Unpacking Argument Lists:
# def myfunc(start,stop):
# 	print(start)
# 	print(stop)	

# args = [3, 9]
# myfunc(*args)
# myfunc(3,9)
# print(list(range(*args)))
# range(start,stop,step)

'''In the same fashion, dictionaries can deliver keyword arguments 
with the **-operator:'''
def bestof2010s(got, brekbad='Jesse', theoffice='Michael'):
	print(f"my favourite G.O.T character: {got}")
	print(f"my favourite breaking bad character: {brekbad}")
	print(f"my favourite the office character: {theoffice}")

d = {"got": "Cersei", "brekbad": "W.W", "theoffice": "Dwight"}
bestof2010s(got="Cersei",brekbad="W.W", theoffice="Dwight")
bestof2010s(**d)