from pathlib import Path
import logging
from logging.config import fileConfig
configpath = Path(__file__).absolute().parent / 'logging_config.ini'

fileConfig(configpath)

logger = logging.getLogger(__name__)
logger.debug("Logging Configured")