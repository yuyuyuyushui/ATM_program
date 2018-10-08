
from core.transaction import *
from conf import settings
from .accounts import read_meassage
from .logger import logger
def main_():
    dict_opreation = [
        ("转账",transfer_accounts),
    ("还款", repayment),
    ("取款", withdraw_money),
    ("查询", query_money),
    (  "账单", pay_check)
    ]
    while not settings.LOGGING_STATE['admin']:
        admin = input("请输入用户名》》")
        passed = input('请输入密码》》')
        date = read_meassage(admin)
        if date and date['password'] == passed:
            settings.LOGGING_STATE["admin"] = True
            while True:
                for index,val in enumerate(dict_opreation):
                    print(index, val[0])
                chioce_op = input('请输入你选择的操作》》').strip()
                if int(chioce_op)>=0 and int(chioce_op)<len(dict_opreation):
                    dict_opreation[int(chioce_op)][1](date)
                elif chioce_op == 'exit':
                    settings.LOGGING_STATE["admin"] = False
                    break
                else:
                    logger(settings.LOG_TYPES['transaction']).error('输入的参数有问题')
                    print('你输入的选择有误，')
        else:
            print("请输入正确的账号")
if __name__=="__main__":
    main_()