#用于从文件里加载和存储账户数据
import os,sys,json
def read_meassage(admin):
    dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    dir_path = dir_path +  r'\db\accounts'
    if admin in os.listdir(dir_path):
        dir_path += "\\"
        dir_path += admin
        print(dir_path)
        with open(dir_path, 'r', encoding='utf-8') as f:
            h = json.load(f)
        return h
    else:
        print('false')
        return False
if __name__ == "__main__":
    read_meassage('1234')

