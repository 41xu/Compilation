# e表示空串
"""
E->TE'
E'->+TE'|e
T->FT'
T'->*FT'|e
F->(E)|id

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

"""

import pandas as pd
#预测分析表
constract_table=pd.DataFrame({
    'id':["E -> T E'","error","T -> F T'","error","F -> id"],
    '+':["error","E' -> + T E'","synch","T' -> e","synch"],
    '*':["error","error","error","T' -> * F T'","synch"],
    '(':["E -> T E'","error","T -> F T'","error","F -> ( E )"],
    ')':["synch","E' -> e","synch","T' -> e","synch"],
    '$':["synch","E' -> e","synch","T' -> e","synch"],
},index=['E',"E'","T","T'",'F'],columns=['id','+','*','(',')','$'])
# print(constract_table)

# text="id * id + id $"
# text="id + id $"
# text="id + id  * id $"
text="id id * id $" #错误验证部分
# text="id * * id $"
# text="( id + id $"
text=text.split()
# print(text)
t=iter(text)
cur=next(t)

stack=[]
stack.append("$")
result=[]


def error():
    pass

#先把E开始符号加进去
stack.append("E")

#开始按表分析了！

while stack[-1]!="$":
    print("分析器每次查表之前的stack")
    print(stack)
    # print(cur)
    if stack[-1]!=cur: #栈顶这里肯定是非终结符，cur是终结符，因此要发生匹配 这个if里肯定是预测分析表里能看见的 没有error的
        add=constract_table.loc[stack[-1]][cur]
        if add!="error" and add!="synch":
            result.append(add)
            temp=add.split("->")
            # print(temp)
            wait_to_add_in_stack=temp[-1].split()
            # print(wait_to_add_in_stack)
            stack.pop()
            if wait_to_add_in_stack[-1]!="e":
                for i in range(len(wait_to_add_in_stack)):
                    stack.append(wait_to_add_in_stack[len(wait_to_add_in_stack)-i-1]) #->符号右边的一坨东西按照倒序加进stack里
            else:
                # print("当前栈顶的非终结符产生了空串呢")
                #这里就不将生成空串的空串加进stack了！
                pass
        # if stack[-1]==")":
        #     # print("用户输入出现错误！！！下面进入错误恢复...")
        #     # print("*\...*\...*\...")
        #     print("这位朋友，你看看你输入了个什么东西！你的')'呢！！！")
        #     stack.pop()
        else:
            #这里就出现错误了，具体情况是：栈顶是非终结符A，cur输入符号是a，而M[A,a]现在是空白的error
            print("用户输入出现错误！！！下面进入错误恢复...")
            print("*\...*\...*\...")
            if add=="error":
                print("这位朋友，你好像多输入了一个字符"+cur+"呀！现在把这个字符弹出去了！")
                cur=next(t)
            if add=="synch":
                print("这位朋友，你好像少输入了什么东西呀！")
                stack.pop()


    else:
        print("匹配"+str(cur)+"将其弹出")
        stack.pop()
        # print(cur)
        if cur!="$":
            cur=next(t)
        #这里得添加iterate的异常处理StopIteration
        # try:
        #     cur=next(t)
        # except StopIteration:
        #     pass
        #但是我们发现判断是不是$其实本身就是在判断还能不能迭代下去了呢 所以不用加except！
    print("分析器每次查表之后的stack")
    print(stack)
print(result)