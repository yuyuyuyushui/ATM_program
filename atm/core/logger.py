#日志记录模块
import logging
#生成日志对象
loger = logging.getLogger('test_log')
#生成formater对象
formater = logging.Formatter("%(asctime)s-%(name)s-%(levelname)s-%(message)s")

#生成文件handler
fh = logging.FileHandler('web.log')
#生成流式handler
sh = logging.StreamHandler()
#handler添加输出格式
fh.setFormatter(formater)
sh.setFormatter(formater)
#添加handler到loger对象中
loger.addHandler(fh)
loger.addHandler(sh)
#设置日志级别
loger.setLevel(logging.INFO)

loger.error('this is error')


