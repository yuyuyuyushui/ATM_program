#日志记录模块
# import logging
# #生成日志对象
# loger = logging.getLogger('test_log')
# #生成formater对象
# formater = logging.Formatter("%(asctime)s-%(name)s-%(levelname)s-%(message)s")
#
# #生成文件handler
# fh = logging.FileHandler('web.log')
# #生成流式handler
# sh = logging.StreamHandler()
# #handler添加输出格式
# fh.setFormatter(formater)
# sh.setFormatter(formater)
# #添加handler到loger对象中
# loger.addHandler(fh)
# loger.addHandler(sh)
# #设置日志级别
# loger.setLevel(logging.INFO)
#
# loger.error('this is error')
import logging
from conf import settings
def logger(logging_name):
    loger_path = "%s\log\%s"%(settings.DIR_PATH,logging_name)
    print(loger_path)
    loger = logging.getLogger(logging_name)
    formater = logging.Formatter("%(asctime)s-%(name)s-%(levelname)s-%(message)s")
    fh = logging.FileHandler(loger_path)
    sh = logging.StreamHandler()
    fh.setFormatter(formater)
    sh.setFormatter(formater)
    loger.addHandler(fh)
    loger.addHandler(sh)
    loger.setLevel(logging.INFO)
    return loger




