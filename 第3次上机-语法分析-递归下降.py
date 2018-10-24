# e表示空串
"""
E->TE'
E'->+TE'|e
T->FT'
T'->*FT'|e
F->(E)|id
"""

import sys
sys.setrecursionlimit(999999999)

rule = [
    "E->TE_",  # 0
    "E_->+TE_",  # 1
    "E_->e",  # 2
    "T->FT_",  # 3
    "T_->*FT_",  # 4
    "T_->e",  # 5
    "F->(E)",  # 6
    "F->id",  # 7
]

firstE = ['(', 'id']
firstE_ = ['+', '']
firstT = ['(', 'id']
firstT_ = ['*', '']
firstF = ['(', 'id']
followE = ['$', ')']
followE_ = ['$', ')']
followT = ['+', '']
followT_ = ['+', '']
followF = ['*', '']

result = []

text = "id + id #"
text = text.split()
t = iter(text)
global cur

cur = next(t)


def E():
    global cur
    if cur in firstE:
        result.append(rule[0])
        T()
        E_()
    else:
        return False


def E_():
    global cur
    if cur=='#':
        result.append(rule[2])
        return
    if cur == '+':
        result.append(rule[1])
        T()
        E_()
    if cur == '':
        result.append(rule[2])
    else:
        if cur in followE_:
            cur = next(t)
            return True
        else:
            return False


def T():
    global cur
    if cur in firstT:
        result.append(rule[3])
        F()
        # cur=next(t)
        T_()
    else:
        if cur in followT:
            result.append(rule[3])
            cur = next(t)
            F()
            T_()
            return True
        else:
            return False


def T_():
    global cur
    cur=next(t)
    if cur=='#':
        result.append(rule[5])
        return
    if cur == '*':
        result.append(rule[4])
        cur=next(t)
        F()
        T_()
    if cur == '':
        result.append(rule[5])
        cur=next(t)

    else:
        if cur in followT_:
            result.append(rule[5])
            return True
        else:
            return False


def F():
    global cur
    if cur == '(':
        result.append(rule[6])
        E()
    if cur == 'id':
        result.append(rule[7])
    else:
        return False


E()
print(result)
