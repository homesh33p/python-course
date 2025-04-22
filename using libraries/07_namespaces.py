'''
A namespace is a mapping from names to objects.
The important thing to know about namespaces is that there is absolutely
no relation between names in different namespaces;
for instance, two different modules may both define a function maximize
without confusion — users of the modules must prefix it with the module name.

'''
# from toimportfrom import myattr
# myattr = 2
# myvariable = 3
# print(myattr)

# # or

# import toimportfrom
# toimportfrom.myattr = 3
# print(toimportfrom.myattr)

'''
By the way, I use the word attribute for any name following a dot — for example,
in the expression z.real, real is an attribute of the object z.
Strictly speaking, references to names in modules are attribute references:
in the expression modname.funcname, 
modname is a module object and funcname is an attribute of it
'''

# # Can be deleted:
# import toimportfrom
# del toimportfrom.myattr

# try:
# 	print(toimportfrom.myattr)
# except:
# 	print("attribute deleted")

# # Can be created:
# import toimportfrom
# toimportfrom.newattr = 2

# print(toimportfrom.newattr)

# # Check what atrtibutes are present:
# import toimportfrom
# print(dir(toimportfrom))
# toimportfrom.newattr = 2
# print(dir(toimportfrom))
# print(toimportfrom.__name__)


'''
 In above case there happens to be a straightforward mapping between 
 the module’s attributes and the global names defined in the module:
 they share the same namespace! 
'''

'''
The local namespace for a function is created when the function is called,
and deleted when the function returns or raises an exception that is not handled within the function.
(Actually, forgetting would be a better way to describe what actually happens.)
Of course, recursive invocations each have their own local namespace.
'''

'''
A scope is a textual region of a Python program where a namespace is directly accessible.
“Directly accessible” here means that an unqualified reference to a name attempts to find the name in the namespace.

Although scopes are determined statically, they are used dynamically.
At any time during execution, there are 3 or 4 nested scopes whose namespaces are directly accessible:
'''
# >    the innermost scope, which is searched first, contains the local names

# def innerfunc():
# 	innerattr = 1 	#its the innermost scope only accessible within the function,
# 					# Can be called with unqualified call(no module name atached before), within the function


'''
 >  the scopes of any enclosing functions, which are searched starting with the
	nearest enclosing scope, contains non-local, but also non-global names
'''

# def wrapper():
# 	outerattr = 1 #This is in the scope of the enclosing function

# 	def innerfunc():
# 		innerattr = 2
# 		print(f"outerattr: {outerattr}")
# 		print(f"Innerattr: {innerattr}")

# 	innerfunc()

# wrapper()

''' 
 >   the next-to-last scope contains the current module’s global names
'''

# globalattr = 1 #Global attr

# def wrapper():
# 	outerattr = 1 #This is in the scope of the enclosing function

# 	def innerfunc():
# 		innerattr = 2
# 		print(f"globalattr: {globalattr}")		
# 		print(globalattr)

# 	innerfunc()

# wrapper()

'''
 >  the outermost scope (searched last) is the namespace containing built-in names
	like __name__, or inbuilt functions like int,str,list,dict.....
'''

'''
Further read about the local and global namespace and keywords like global,nonlocal:
https://docs.python.org/3/tutorial/classes.html
'''