import logging

__version__ = '2.0.1'

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

logging.info('zn-p2 %s' % __version__)
from .imp import *
