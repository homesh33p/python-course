from pathlib import Path,PurePath
import pickle
import logging

from ..factory.diskdbutility.handler import Handler
logger = logging.getLogger(__name__)

class Initialise:
	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		thisfilepath = Path(__file__).absolute()
		self._templatefolder = thisfilepath.parent / "templates"

	def createdummy(self):
		for file in list(self._templatefolder.glob('**/*.pkl')):
			filename = PurePath(file).stem
			handle = Handler(document=filename)
			if not handle.identify():
				logger.info("Creating dummy data in the database for the file: %s"%(filename))
				with open(file, 'rb') as template:
					data = pickle.load(template)
				handle.storefile(data=data,create=True)

if __name__=="__main__":
	Initialise().createdummy()