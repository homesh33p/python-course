import pickle
import logging

from .dbutil import Dbcore
from ..dictparserutil.dictparser import Dictparser

logger = logging.getLogger(__name__)

class Handler(Dbcore,Dictparser):

	def __init__(self,**kwargs):
		super().__init__(document=kwargs["document"])
		self.getconnection()
		self.data = None

	def identify(self):
		if self._docpath.exists():
			return True
		return False

	def storefile(self, data, create=False):
		logger.debug("Attempting to store document: %s"%(self.docname))
		if not self.identify():
			logger.warning("Document %s does not exist"%self.docname)
			if not create:
				raise FileNotFoundError("Document %s does not exist"%self.docname)
			logger.info("Creating document %s"%self.docname)
		self.data = data
		self._docpath.parent.mkdir(parents=True,exist_ok=True)
		with open(self._docpath, 'wb') as filehandler:
			pickle.dump(self.data, filehandler)
			logger.debug("Stored %s successfully"%(self.docname))

	def retrievefile(self):
		if not self.identify():
			logger.warning("Document %s does not exist"%self.docname)
			raise FileNotFoundError("Document %s does not exist"%self.docname)
		with open(self._docpath, 'rb') as filehandler:
			self.data = pickle.load(filehandler)
		return self.data