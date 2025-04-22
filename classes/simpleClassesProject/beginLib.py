import logging

logging.basicConfig(level=logging.INFO)

from sample.library.library import Library

logger = logging.getLogger(__name__)

if __name__ == "__main__":
	Library().begin()