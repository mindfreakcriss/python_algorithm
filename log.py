# coding=utf-8
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

fh=logging.FileHandler('log_test.log')
fh.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)

logger.addHandler(fh)
logger.addHandler(ch)

# 还能进行其他信息的输出，参考日志文件

logger.debug("调试信息")
logger.info('一般信息')
logger.warning("警告信息")
logger.error('错误信息')
logger.critical("严重信息")