#记账\还钱\取钱等所有的与账户金额相关的操作
import os
import sys
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(base_dir)
sys.path.append(base_dir)
from core import auth
@auth.login
def transfer_accounts():
    return 1
def repayment():
    pass
def withdraw_money():
    pass
def query_money():
    pass