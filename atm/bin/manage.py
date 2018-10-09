#atm管理端，未实现
import os,sys
dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dir_path)
def manage():
    while True:
        admin = input('请输入管理员账号》》')
        password = input("请输入管理员密码》》")
        if admin =='admin'and password == '1234':

