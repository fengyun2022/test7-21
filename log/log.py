import logging
from config.config import log_path

#新建日志器
logger=logging.getLogger()
#设置日志的级别(INFO信息，DEBUG调试，WARNING警告，CRITICAL严重，ERROR错误信息
logger.setLevel(logging.INFO)
##日志的格式
format=logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
##设置日志文件的地址
logFile = log_path
##打开日志文件
fh = logging.FileHandler(logFile, mode='a', encoding='utf-8')
##日志文件记录日志的级别
fh.setLevel(logging.INFO)
##日志文件记录的格式
fh.setFormatter(format)
##添加日志内容
logger.addHandler(fh)