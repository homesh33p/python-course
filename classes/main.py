from sample.factory.loggingutility.loggerutil import *
from sample.library.library import Library

import logging
logger = logging.getLogger(__name__)

if __name__ == "__main__":
	Library().begin()