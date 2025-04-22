'''
A person class
'''

class Person:

	def __init__(self, f_name, l_name):
		self.first_name = f_name
		self.last_name = l_name

	def get_name(self):
		return self.first_name + " " + self.last_name


'''
An employee class
'''

# class Employee(Person):
#
# 	def __init__(self, f_name, l_name, emp_id, emp_title):
# 		Person.__init__(self, f_name, l_name)
# 		self.employee_id = emp_id
# 		self.title = emp_title
#
# 	def isEmployee(self):
# 		return True


'''
All the attributes and methods of person are avaialble to the
employee class
'''

# e1 = Employee("Alex", "Branden", 23456, 'Director')
# print(e1.first_name)
# print(e1.last_name)
# print(e1.get_name())

'''
Initializing, parent class attributes in child class:
by using super() built-in function, like below.
 
super().__init__(f_name, l_name)

 
Above we are calling __init__ method without class name,

super() resolves parent class name,

with Method Order Resolution (MRO) technique. 
'''
#
# class Employee(Person):
#
# 	def __init__(self, f_name, l_name, emp_id, emp_title):
# 		super().__init__(f_name,l_name)
# 		self.employee_id = emp_id
# 		self.title = emp_title
#
# 	def isEmployee(self):
# 		return True
# #
# e1 = Employee("Alex", "Branden", 23456, 'Director')
# print(e1.first_name)
# print(e1.last_name)
# print(e1.get_name())

'''
method overriding:
'''
#
# class A:
#
# 	def __init__(self):
# 		self.__x = 1
#
# 	def m1(self):
# 		print("m1 from A")
#
#
# class B(A):
# 	def __init__(self):
# 		super().__init__()
# 		self.__y = 1
#
# 	def m1(self):
# 		print("m1 from B")
#
# c = B()
# c.m1()

'''
The isinstance() function is used to determine whether the object is an instance of the class or not.
'''
# print(isinstance(1, int))
# print(isinstance(c,B))

'''
“Private” instance variables that cannot be accessed 
except from inside an object don’t exist in Python.
However, there is a convention that is followed by most Python code: 
a name prefixed with an underscore (e.g. _spam)
should be treated as a non-public part of the API 
(whether it is a function, a method or a data member).
'''

class A:

	def __init__(self):
		self.__x = 1

	def m1(self):
		print("m1 from A")

	def _updatex(self,val):
		self.__x = val
#
class B(A):
	def __init__(self):
		super().__init__()
		self._updatex(2)
		self.__y = 1

	def m1(self):
		print("m1 from B")

c = B()
print(c.__y)
c.m1()