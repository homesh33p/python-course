import logging
from ..utilities.diskdbutility.handler import Handler
from ..utilities.dictparserutil.dictparser import Dictparser

logger = logging.getLogger(__name__)

class Books:
	def __init__(self,**kwargs):
		handler = Handler(document="books")
		self.__books = handler.retrievefile()
		self.book = kwargs["book"]
		self.dept = kwargs.get("department")
		self.subdept = kwargs.get("subdepartment")
		assert self.dept or self.subdept
		self.__section = self.dept or self.subdept

	def fetchbook(self):
		dictparser = Dictparser()
		sectionpath,section,sectiondata = dictparser.findindict(data=self.__books,key=self.__section)
		if not section:
			logger.warning("%s department does not exist"%(self.__section))
			self.bookpath, self.bookid = None,None
			return self.bookpath, self.bookid
		logger.debug("Section Path=%s"%sectionpath)
		logger.debug("section data: %s"%sectiondata)
		bookpath,bookid,bookname = dictparser.findindict(data=sectiondata,val=self.book)
		if not bookid:
			logger.warning("%s book not found in the library"%self.book)
			self.bookpath, self.bookid = None, None
			return self.bookpath, self.bookid
		logger.debug("book path=%s" %bookpath)
		bookpath = sectionpath+bookpath
		self.bookpath, self.bookid = bookpath,bookid
		return self.bookpath, self.bookid

