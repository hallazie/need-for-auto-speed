# coding:utf-8

import logging
import warnings


logger = logging.getLogger(__file__)
logging.basicConfig(format='%(asctime)-15s %(levelname)s %(lineno)d %(message)s')
warnings.filterwarnings('ignore', category=UserWarning)
