import logging

from .books import Books
from .students import Students

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

class Library:

	def operations(self,choice):
		name = input("Your name:")
		roll = Students().getrollnum(name)
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

		bookobj = Books(department=dept,subdepartment=subdept,book=bookname)
		bookpath, bookid = bookobj.fetchbook()
		if not bookid:
			logger.info(f"Book doesnot exist: {bookname}")
			return
		logger.info(f"Book id: {bookid}")

	def begin(self):
		logger.info("Library open!")
		choice = input("How can i help you? options: Findbook(more options coming soon)")
		while choice.lower() in ["findbook"]:
			self.operations(choice=choice.lower())
			choice = input("Continue? choices: Findbook,exit")
		logger.info("Have a nice day!")





