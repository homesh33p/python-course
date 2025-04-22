import pickle
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

class Handler:

	def __init__(self,document):
		self.__dbpath = Path("sample") / "database"
		self.docname = document
		self._docpath = self.filepath()
		self.data = None

	def filepath(self):
		self._docpath = Path(self.__dbpath) / (self.docname+".pkl")
		return self._docpath

	def identify(self):
		if self._docpath.exists():
			return True
		return False

	def retrievefile(self):
		if not self.identify():
			logger.warning("Document %s does not exist"%self.docname)
			raise FileNotFoundError("Document %s does not exist"%self.docname)
		with open(self._docpath, 'rb') as filehandler:
			self.data = pickle.load(filehandler)
		return self.data