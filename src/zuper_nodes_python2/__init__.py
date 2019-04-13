import logging

__version__ = '2.0.0'

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

logging.info('zuper-nodes-python2 %s' % __version__)
from .imp import *
