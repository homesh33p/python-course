# class Test:
#
# 	def myfunc():
# 		print("it worked!")
#
# Test.myfunc()

'''
When a class definition is entered, a new namespace is created,
and used as the local scope — thus, all assignments to local variables
go into this new namespace. 
In particular, function definitions bind the name of the new function here.
'''

# class Test:
#
# 	classatrr = 2
#
# 	def myfunc():
# 		print("Class attr : %d"%(classatrr))
#
# print(Test.classatrr)


'''
Printing via an instance
'''

# import traceback
# try:
# 	Test.myfunc()
# except:
# 	traceback.print_exc()
#
# instance1 = Test()
# instance2 = Test()
#
# print(instance2.classatrr)
# print(instance1.classatrr)


'''
To access the class variable, pass the self keyword:
'''
# class Test:
#
# 	classatrr = "class attribute"
#
# 	def myfunc(self):
# 		print("Class attr : %s"%(self.classatrr))
#
# Test().myfunc()


'''
But class variables are shared by all instances
'''
# class Test:
#
# 	classatrr = "class attribute"
#
# 	def myfunc(self):
# 		print("Class attr : %s"%(self.classatrr))
#
# 	def setclassattr(self,val):
# 		self.classatrr = val
#
# Test().myfunc()
# instance1 = Test()
# instance2 = Test()

'''
Class variables cannot be changed by an instance, insted it creates a new variable
for that instance that shadows the class variable
'''

# instance2.setclassattr("Changed by instance2")
#
# print(instance2.classatrr)
# print(instance1.classatrr)

'''
Class variables can be changed by reference to the class itself
'''

# Test.classatrr = "Changed by class"
#
# print(instance2.classatrr)
# print(instance1.classatrr)

'''
To bind a variable to an instance, use the self keyword
'''

# class Test:
#
# 	def __init__(self):
# 		self.instatrr = "Instance attribute"
#
# 	def printinstattr(self):
# 		print("Instance attr : %s"%(self.instatrr))
#
# 	def setinstattr(self,val):
# 		self.instatrr = val
#
# instance1 = Test()
# instance2 = Test()
#
# instance1.setinstattr("Changed by inst1")
# instance1.printinstattr()
# instance2.printinstattr()

# instance2.instatrr = "Changed by inst2"
# instance2.printinstattr()

'''
Bound and unbound methods
'''

# print(Test.printinstattr)
# Test.printinstattr()

'''
lets try:
'''

# Test.printinstattr(2)


'''
lets try:
'''

# Test.printinstattr()

'''
It worked! We called the method with an instance as its first argument,
so everything's fine.
But you will agree with me if I say this is not a very handy way to call methods;
we have to refer to the class each time we want to call a method. And 
if we don't know what class is our object, this is not going to work for very long.

So what Python does for us, is that it binds all the methods 
from the class Test to any instance of this class.
This means that the attribute get_size of an instance of Test is a bound method:
a method for which the first argument will be the instance itself.

'''

# print(Test().printinstattr)

'''
But what if you wanted to know which object this bound method is bound to?
'''
# a = Test()
# print(a.printinstattr.__self__)

'''
__init__() is used to set values or call functions when the class instance is created
'''
# class Test:
#
# 	def __init__(self,somevalue):
# 		self.instatrr = somevalue
#
# 	def printinstattr(self):
# 		print("Instance attr : %s"%(self.instatrr))
#
# 	def setinstattr(self,val):
# 		self.instatrr = val
#
#
# inst1 = Test("value while initialising")
# inst1.printinstattr()


'''
You can also call functions inside the __init__()
make any values referenced by the function is initialised before the function call
'''
class Test:

	def __init__(self,somevalue):
		self.instatrr = somevalue
		self.printinstattr()
		self.setinstattr(2)
		self.printinstattr()
		print(self.instatrr)

	def printinstattr(self):
		print("Instance attr : %s"%(self.instatrr))

	def setinstattr(self,val):
		self.instatrr = val

inst = Test("value while initialising")

