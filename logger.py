import logging
import os.path
import sys
from datetime import datetime


def setup_logging():
    debugging = 'pydevd' in sys.modules or 'pdb' in sys.modules

    logger = logging.getLogger('cyber_empire')
    logger.setLevel(logging.DEBUG if debugging else logging.INFO)

    if not os.path.exists('logs'):
        os.mkdir('logs')
    fh = logging.FileHandler(f'logs/cyber_empire.log')
    fh.setLevel(logging.DEBUG if debugging else logging.INFO)

    ch = logging.StreamHandler()
    ch.setLevel(logging.WARNING)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    logger.addHandler(fh)
    logger.addHandler(ch)
