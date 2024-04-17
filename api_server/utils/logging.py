import logging
import sys

def init_logger(name: str, level="DEBUG", format='[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s'):
    logger = logging.getLogger(name)
    if not logger.hasHandlers():
        # add stdout handler
        handler = logging.StreamHandler(sys.stdout)
        # set handler format
        logFormatter = logging.Formatter(fmt=format)
        handler.setFormatter(logFormatter)
        logger.addHandler(handler)
        # set logger level
        if type(level) == str:
            logger.setLevel(logging.getLevelName(level))
        elif level is not None:
            logger.setLevel(level)
    return logger