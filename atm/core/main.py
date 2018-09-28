import sys, os
dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dir_path)
from core.transaction import *
def main():

    print(sys.path)
    df = {
        1: "转账",
        2: "还款",
        3: "取款",
        4: "查询"
    }
    dict_opreation = {
        1: transfer_accounts,
        2: repayment,
        3: withdraw_money,
        4: query_money
    }
    while True:
        for i in df:
            print(i, df[i])
        chioce_op = input('请输入你选择的操作》》').strip()
        if int(chioce_op) in dict_opreation:
            dict_opreation[int(chioce_op)]()
if __name__=="__main__":
    main()