"""
E->E+T|T
T->T*F|F
F->(E)|id
"""
import pandas as pd
import re

data = pd.DataFrame({
    'id': ["s5", "error", "error", "error", "s5", "error", "s5", "s5", "error", "error", "error", "error"],
    '+': ["error", "s6", "r2", "r4", "error", "r6", "error", "error", "s6", "r1", "r3", "r5"],
    '*': ["error", "error", "s7", "r4", "error", "r6", "error", "error", "error", "s7", "r3", "r5"],
    '(': ['s4', 'error', 'error', 'error', 's4', 'error', 's4', 's4', 'error', 'error', 'error', 'error'],
    ')': ['error', 'error', 'r2', 'r4', 'error', 'r6', 'error', 'error', 's11', 'r1', 'r3', 'r5'],
    '$': ['error', 'acc','r2', 'r4', 'error', 'r6', 'error', 'error', 'error', 'r1', 'r3', 'r5'],
    'E': ['1', 'error', 'error', 'error', '8', 'error', 'error', 'error', 'error', 'error', 'error', 'error'],
    'T': ['2', 'error', 'error', 'error', '2', 'error', '9', 'error', 'error', 'error', 'error', 'error'],
    'F': ['3', 'error', 'error', 'error', '3', 'error', '3', '10', 'error', 'error', 'error', 'error']
})

#产生式
rules={
    1:"E -> E + T",
    2:"E -> T",
    3:"T -> T * F",
    4:"T -> F",
    5:"F -> ( E )",
    6:"F -> id"
}

# print(rules[3].split("->")[-1].split())

# print(data)
# text="id * id / ( id + id ) $" #验证出错
symbol=['id','(',')','*','+','$']
text="id * id + id $"
text=text.split()
text=iter(text)
cur=next(text)
stack=[]
stack.append(0)
result=[]
while 1:
    print(stack)
    if cur not in symbol:
        print("input error. we will drop the top symbol")
        cur=next(text)
        continue
    test=data.loc[stack[-1],cur]
    if test[0]=='s':
        stack.append(cur)
        stack.append(int(test[1:]))
        cur=next(text)
        print("移进",stack[-1])
    elif test[0]=='r':
        rul=int(test[1:])#具体的对应哪个规约
        #stack先弹出来对应规则右边的那么多个长度
        pop_len=len(rules[rul].split("->")[1].split())*2
        while pop_len>0:
            stack.pop()
            pop_len-=1
        stack.append(rules[rul].split("->")[0].split()[0])
        stack.append(int(data.loc[stack[-2],stack[-1]]))
        print(stack)
        result.append(rules[rul])
        print("规约")
        print(rules[rul])
    elif test[0]=='a':
        break
    else:
        print("error")
        cur=next(text)
print(result)





