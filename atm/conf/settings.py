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