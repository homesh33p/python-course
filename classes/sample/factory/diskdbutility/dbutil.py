'''
factory
'''
import logging
from pathlib import Path
logger = logging.getLogger(__name__)

from ..configutility.configutil import Configutil

class Dbcore:

	def __init__(self,document):
		config = Configutil().getconfig()
		self.__dbpath = config["DBSection"]["url"]
		self.docname = document
		self._docpath = None

	def getconnection(self):
		self._docpath = Path(self.__dbpath) / (self.docname+".pkl")
		return self._docpath
