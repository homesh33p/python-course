# Logging in python:

# refer: https://docs.python.org/3/howto/logging.html
#        https://docs.python.org/3/library/logging.html

# setting the logging config in a dictionary or file:
# https://docs.python-guide.org/writing/logging/
# logging in depth, using filters and mltithreading and child loggers: https://docs.python.org/3.8/howto/logging-cookbook.html


# A very simple example is:

import logging
# logging.warning('Watch out!')  # will print a message to the console
# logging.info('I told you so')  # will not print anything

# # The INFO message doesn’t appear because the default level is WARNING.
#
# # Logging to file:
# logging.basicConfig(filename='example.log', level=logging.DEBUG)
# logging.debug('This message should go to the log file')
# logging.info('So should this')
# logging.warning('And this, too')
# logging.error('And non-ASCII stuff, too, like Øresund and Malmö')
#
# A good convention to use when naming loggers is to use a module-level logger, in each module which uses logging, named as follows:

logger = logging.getLogger(__name__)

# These are the most common configuration methods:

# Logger.setLevel() specifies the lowest-severity log message a logger will handle, where debug is the lowest built-in severity level and critical is the highest built-in severity. For example, if the severity level is INFO, the logger will handle only INFO, WARNING, ERROR, and CRITICAL messages and will ignore DEBUG messages.

# Logger.addHandler() and Logger.removeHandler() add and remove handler objects from the logger object.

# Logger.addFilter() and Logger.removeFilter() add and remove filter objects from the logger object.
#
# # sample code for using handlers and formatters->
#
# import logging
#
# # create logger
# logger = logging.getLogger('simple_example')
# logger.setLevel(logging.DEBUG)
#
# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
#
# # create formatter
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#
# # add formatter to ch
# ch.setFormatter(formatter)
#
# # add ch to logger
logger.addHandler(ch)
#
# # 'application' code
# logger.debug('debug message')
# logger.info('info message')
# logger.warning('warn message')
# logger.error('error message')
# logger.critical('critical message')


# VERY IMPORTANT: If you change the config of a logger in any module, 
# it will change the config of all loggers in the application