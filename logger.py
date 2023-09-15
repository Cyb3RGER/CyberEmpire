import logging
import os.path
from datetime import datetime


def setup_logging():
    logger = logging.getLogger('cyber_empire')
    logger.setLevel(logging.DEBUG)

    if not os.path.exists('logs'):
        os.mkdir('logs')
    fh = logging.FileHandler(f'logs/cyber_empire.log')
    fh.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(logging.WARNING)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    logger.addHandler(fh)
    logger.addHandler(ch)
