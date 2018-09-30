
from core.transaction import *
from conf import settings
from .accounts import read_meassage
def main_():
    df = {
        1: "转账",
        2: "还款",
        3: "取款",
        4: "查询",
        5: "账单"
    }
    dict_opreation = {
        1: transfer_accounts,
        2: repayment,
        3: withdraw_money,
        4: query_money,
        5: pay_check
    }
    while not settings.LOGGING_STATE['admin']:
        admin = input("请输入用户名》》")
        passed = input('请输入密码》》')
        date = read_meassage(admin)
        if date['password'] == passed:
            settings.LOGGING_STATE["admin"] = True
            for i in df:
                print(i, df[i])
            chioce_op = input('请输入你选择的操作》》').strip()
            if int(chioce_op) in dict_opreation:
                dict_opreation[int(chioce_op)]()
        else:
            print("请输入正确的账号")
if __name__=="__main__":
    main_()