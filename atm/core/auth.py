#用户验证
# import  os,sys
# dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(dir_path)
from conf.settings import *
from core import accounts

def login(func):
    def longging(*args,**kwargs):
        if LOGGING_STATE['admin']:
            return func(*args, **kwargs)
        else:
            admin = input("请输入用户名")
            passwd = input("请输入登录密码")
            date = accounts.read_meassage(admin)
            print(date)
            if date and date['password'] == passwd:
                LOGGING_STATE['admin'] = True
                print(args)
                return func(*args, **date)
            else:
                print("你输入的参数有误")
    return longging
