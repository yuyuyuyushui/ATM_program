#用于从文件里加载和存储账户数据
import os,sys,json
def read_meassage(admin):
    dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    dir_path = dir_path + '\\' + 'db'
    if admin in os.listdir(dir_path):
        dir_path += "\\admin"
        with open(dir_path, 'r',encoding='utf-8') as f:
            for i in f:

    else:
        return False

