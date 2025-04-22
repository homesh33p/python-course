from ..factory.diskdbutility.handler import Handler

'''
Faculty rollnum starts from 101
'''

class Faculties(Handler):
	def __init__(self):
		super().__init__(document="faculty")
		self.faculties = self.retrievefile()
		self.faculties = [faculty.lower() for faculty in self.faculties]

	def getrollnum(self,name):
		name = name.lower()
		if name in self.faculties:
			return self.faculties.index(name)+101

	def getname(self,rollnum):
		if not rollnum <= len(self.faculties):
			return
		return self.faculties[rollnum-101]