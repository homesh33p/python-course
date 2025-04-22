import datetime
import pytz
import logging

from ..factory.diskdbutility.handler import Handler
from .books import Books

IST = pytz.timezone('Asia/Kolkata')

logger = logging.getLogger(__name__)

class Register(Handler):
	def __init__(self,**kwargs):
		super().__init__(**kwargs,document="register")

		self.path = kwargs["path"]
		self.register = self.retrievefile()

	def submit(self):
		path,key,val = self.findindict(data=self.register,path=self.path)
		if not key:
			raise KeyError("Path: %s not found in register"%(self.path))

		if not val:
			logger.warning("book not issued, cannot submit what has not been issued")
			return

		subDate = datetime.datetime.strptime(val["Submission Date"],"%d-%b-%Y")
		currenttime = datetime.datetime.now(IST)

		diff = currenttime - IST.localize(subDate)
		daydiff = diff.days
		if daydiff>0:
			logger.info("Book submitted late by %d days"%(daydiff))

		self.setval(data=self.register,path=self.path,val=None)
		self.storefile(data=self.register)

		logger.info("Thank you for submitting the book")

		return daydiff

	def checkout(self,rollnum,submitafterdays):
		path,key,val = self.findindict(data=self.register,path=self.path)
		if not key:
			raise KeyError("Path: %s not found in register"%(self.path))

		if val:
			logger.warning("book is already issued: %s"%str(val))
			return

		issueDate = datetime.datetime.now(IST)

		subDate = issueDate +datetime.timedelta(days=submitafterdays)
		val = {}
		val["Issued on"] = datetime.datetime.strftime(issueDate,"%d-%b-%Y")
		val["Submission Date"] = datetime.datetime.strftime(subDate,"%d-%b-%Y")
		val["Checked Out By"] = rollnum
		self.setval(data=self.register,path=self.path,val=val)
		self.storefile(data=self.register)

		logger.info("Dont forget to submit the book before: %s"%datetime.datetime.strftime(subDate,"%d-%b-%Y"))
		return True
