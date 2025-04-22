import configparser
from pathlib import Path,PurePath
import logging

logger = logging.getLogger(__name__)

class Configutil:
	def __init__(self):
		self.config = configparser.ConfigParser()
		self.config.read('info.config')

	def __converttodict(self,parser):
		confdict = {section: dict(parser.items(section)) for section in parser.sections()}		
		return confdict

	def getconfig(self):
		confdict = self.__converttodict(self.config)
		dbpath = self.config.get("DBSection","url")
		
		if not PurePath(dbpath).is_absolute():
			try:
				currentdir = Path.cwd()
				dbpath = currentdir / dbpath
			except:
				logger.error("Unable to gather the config")
				raise

		confdict["DBSection"]["url"] = dbpath

		return confdict

	def addconfig(self,parent,key,val):
		logger.info("updating config file")
		assert key not in ["url","coredatabases"]						

		dst = Path.cwd() / "info.config"
		if not self.config.has_section(parent):
			self.config.add_section(parent)

		self.config.set(parent, key, val)
		# Write changes back to file
		with open(dst, 'w') as conf:
			self.config.write(conf)
		logger.info("updated config file successfully")

if __name__ == "__main__":
	configobj = Configutil()
	print(configobj.getconfig())

	# configobj.addconfig(parent="DBSection",key="userdatabases",val="newval")
	# configobj.addconfig(parent="DBSection",key="userdatabases",val="newval")
	configobj.addconfig(parent="Newsection",key="newkey",val="newval")

