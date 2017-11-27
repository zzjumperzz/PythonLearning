#写入标准输出、标准错误
import sys
import logging

#创建logging对象
logger = logging.getLogger(name=__name__)
logger.setLevel(logging.DEBUG)

#创建SteamHeader对象
ch = logging.StreamHandler(stream=sys.stderr)
ch.setLevel(logging.DEBUG)

#创建formatter对象
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

#设置SreeamHeader对象格式
ch.setFormatter(formatter)

#把StreamHeader对象写入loger对象中
logger.addHandler(ch)

def test():
    logger.debug("debug message")
    logger.info("info message")
    logger.warn("warn message")
    logger.error("error message")
    logger.critical("critical message")

test()