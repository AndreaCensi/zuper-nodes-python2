import logging

__version__ = '5.0.14'

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

logger.info('version: %s' % __version__)

from .imp import *
from .outside import *
