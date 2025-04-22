import logging
from ..factory.diskdbutility.handler import Handler

logger = logging.getLogger(__name__)

class Books(Handler):
	def __init__(self,**kwargs):
		super().__init__(**kwargs,document="books")

		self.__books = self.retrievefile()
		self.book = kwargs["book"]
		self.dept = kwargs.get("department")
		self.subdept = kwargs.get("subdepartment")
		assert self.dept or self.subdept
		self.__section = self.dept or self.subdept
		self.__fetchbook()


	def __fetchbook(self):
		sectionpath,section,sectiondata = self.findindict(data=self.__books,key=self.__section)
		if not section:
			logger.warning("%s department does not exist"%(self.__section))
			self.bookpath, self.bookid = None,None
			return
		logger.debug("Section Path=%s"%sectionpath)
		logger.debug("section data: %s"%sectiondata)
		bookpath,bookid,bookname = self.findindict(data=sectiondata,val=self.book)
		if not bookid:
			logger.warning("%s book not found in the library"%self.book)
			self.bookpath, self.bookid = None, None
			return
		logger.debug("book path=%s" %bookpath)
		bookpath = sectionpath+bookpath
		self.bookpath, self.bookid = bookpath,bookid

