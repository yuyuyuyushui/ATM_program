#用户验证
# import  os,sys
# dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(dir_path)
from conf.settings import *
from core import accounts

def login(func):
    def longging(*args,**kwargs):
        if LOGGING_STATE['admin']:
            date = func(*args, **kwargs)
            return date
        else:
            admin = input("请输入用户名")
            passwd = input("请输入登录密码")
            if accounts.read_meassage(admin):
                LOGGING_STATE['admin'] = admin
            else:
                print("你输入的参数有误")
    return longging
