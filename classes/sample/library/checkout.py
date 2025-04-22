from ..factory.diskdbutility.handler import Handler

'''
if they want to issue a book, ask them:
	department: not mandatory if subdepartment available
	subdepartment: not mandatory if department avaialable
	book name: mandatory

if the book is already issued, say sorry and exit
'''


class Checkout:
	def __init__(self,**kwargs):

		self.book = kwargs["book"]
		self.name = kwargs["name"]

	def getrollnum(self):
		students = Handler(document="students").retrievefile()
		faculty = Handler(document="faculty").retrievefile()






