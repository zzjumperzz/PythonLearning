import sys
import logging

path = r'./'
fileName = r'log'

logger = logging.getLogger(name=__name__)
logger.setLevel(logging.DEBUG)

fileheader = logging.FileHandler(r'{0}/{1}.log'.format(path,fileName))
fileheader.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

fileheader.setFormatter(formatter)

logger.addHandler(fileheader)

def test():
    logger.debug("debug message")
    logger.info("info message")
    logger.warn("warn message")
    logger.error("error message")
    logger.critical("critical message")

test()

