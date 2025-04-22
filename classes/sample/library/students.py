from ..factory.diskdbutility.handler import Handler

class Students(Handler):
	def __init__(self):
		super().__init__(document="students")
		self.students = self.retrievefile()
		self.students = [student.lower() for student in self.students]

	def getrollnum(self,name):
		name = name.lower()
		if name in self.students:
			return self.students.index(name)+1

	def getname(self,rollnum):
		if not rollnum <= len(self.students):
			return
		return self.students[rollnum-1]
