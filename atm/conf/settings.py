import os, sys
LOGGING_STATE = {"admin":None,"passwd":None}

DIR_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_TYPES = {
    'transaction': 'transactions.log',
    'access': 'access.log',
}
TRANCE_TYPE = {
    'repay':{'action':'plus', 'interest':0},
    'withdraw':{'action':'minus', 'interest':0.05},
    'transfer':{'action':'minus', 'interest':0.05},
    'consume':{'action':'minus', 'interest':0},
}
MANAGE_CHOICE = {
    '添加账户':'add_accounts',
    "修改额度":"modefy_credit",
    "冻结账户":"frozen_accounts"
}