#用于从文件里加载和存储账户数据
import os,sys,json
from conf import settings


def read_meassage(admin):
    dir_path = r"%s\db\accounts"%(settings.DIR_PATH)
    if admin in os.listdir(dir_path):
        dir_path = '%s\%s'%(dir_path, admin)
        print(dir_path)
        with open(dir_path, 'r', encoding='utf-8') as f:
            date = json.load(f)
        return date
    else:
        print('你输入的账号有问题')
        return False

def write_meassage(accounts_date):
    dir_path = r'%s\db\accounts\%snew'%(settings.DIR_PATH, accounts_date['id'])
    with open(dir_path,'w',encoding='utf-8') as f:
        f.write(json.dumps(accounts_date))
# if __name__ == "__main__":
#     read_meassage('1234')

