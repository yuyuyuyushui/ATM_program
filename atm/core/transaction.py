#记账\还钱\取钱等所有的与账户金额相关的操作
# import os
# import sys
# base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(base_dir)
# sys.path.append(base_dir)
from core import auth
from conf import settings
from core import accounts
@auth.login
def transfer_accounts(accouts_date):
    flag = False
    while not flag:
        trans_money = input('请输入你要转账的金额》》')
        trance_account = input('请输入要转账的账户')
        trance_date = accounts.read_meassage(trance_account)
        if trance_date:
            date = transcation(trans_money,'transfer',accouts_date, **trance_date)
            flag = True
        else:
            print('请输入正确的账户')
def repayment(accounts_date):
    flag = False
    while not flag:
        pay_money = input('请输入你需要还的金额')
        if pay_money.isdigit() and int(pay_money)>0:
            transcation(pay_money,'repayment',accounts_date)
        elif pay_money == 'b':
            flag = True
        else:
            print('输入的金额有问题，请重新输入')
def withdraw_money():
    pass
def query_money():
    pass
def pay_check():
    pass


def transcation(input_money, trans_type, accounts_date,**kwargs):
    input_money = float(input_money)
    if trans_type in settings.TRANCE_TYPE:
        amount = int(input_money) * settings.TRANCE_TYPE[trans_type]['interest']
        amount += input_money
        if settings.TRANCE_TYPE[trans_type]['action'] == 'plus':
            new_balance = accounts_date['balance'] + amount
        elif settings.TRANCE_TYPE[trans_type]['action'] == 'minus':
            if input_money<=accounts_date['balance']:
                new_balance = accounts_date['balance'] - amount
                if kwargs:
                    kwargs['balance'] = float(kwargs['balance'])+input_money
                    accounts.write_meassage(kwargs)
                    print("转账成功")
                else:
                    pass
            else:
                print('你输入的价格超过了余额')
        accounts_date['balance'] = new_balance
        accounts.write_meassage(accounts_date)
        return accounts_date
    else:
        print('')


