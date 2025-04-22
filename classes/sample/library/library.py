import logging

from .initialise import Initialise
from .books import Books
from .register import Register
from .students import Students
from .faculty import Faculties

logger = logging.getLogger(__name__)

'''
1. 

You are the librarian.
A student comes to you. Gives their name.
Asks them if they want to issue a book o submit a book.

if they want to issue a book, ask them:
	department: not mandatory if subdepartment available
	subdepartment: not mandatory if department avaialable
	book name: mandatory

if the book is already issued, say sorry and exit

if book is available, ask:
	Submission Date

Issue the book and update the register accordingly and print it. 
The roll number of the student is their position in the list starting from 1 instead of 0

if they want to submit a book, ask them:
	bookname
	department: not mandatory if subdepartment available
	subdepartment: not mandatory if department avaialable

if submitted on time, tell thank you

if not submitted on time, print the fine:
	if number of days above submission date exceeds 1 week: Warning
	if number of days above submission date exceeds 2 weeks: Monetary fine of Rs. 100
	if number of days above submission date exceeds 3 weeks: Temporary ban of 1 month from library
	if number of days above submission date exceeds 4 weeks: Permanent ban

Update the register and print it.
'''

class Library(Initialise):
	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		self.createdummy()

	def operations(self,choice):
		name = input("Your name:")
		roll = Students().getrollnum(name)
		if not roll:
			roll = Faculties().getrollnum(name)
		if not roll:
			logger.warning("You are not registered for this library")
			return

		dept = input("Department(optional): ")
		subdept = None
		if not dept:
			subdept = input("Subdepartment: ")
			if not subdept:
				return

		bookname = input("book name: ")

		book = Books(department=dept,subdepartment=subdept,book=bookname)
		if not book.bookid:
			return

		if choice == "checkout":
			submitafterdays = int(input("How many days do you wish to keep it?"))
			submitstatus = Register(path=book.bookpath).checkout(rollnum=roll,submitafterdays=submitafterdays)
		else:
			defaulted = Register(path=book.bookpath).submit()

	def begin(self):
		logger.info("Library open!")
		choice = input("How can i help you? options: checkout,submit")
		while choice.lower() in ["checkout","submit"]:
			self.operations(choice=choice.lower())
			choice = input("Continue? choices: checkout,submit,exit")
		logger.info("Have a nice day!")





