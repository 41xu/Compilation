import re
keyword= {"for": 1, "if": 2, "then": 3,"else": 4,"while": 5,
           "do": 6,"until": 29,"int": 30,"input": 31,"output": 32,
           }

operator={":": 17,":=":18,"=": 25,"+": 13,"-": 14,"*": 15,"/": 16,
          "<": 20,">": 23,"<=": 22,"<>": 21,">=": 24,";": 26,
          "(": 27,")": 28,"#": 0,
          }
digits=[chr(i) for i in range(48,58)]
digits="".join(digits)
upper_letter=[chr(i) for i in range(65,91)]
upper_letter="".join(upper_letter)
lower_letter=[chr(i) for i in range(97,123)]
lower_letter="".join(lower_letter)
letter=upper_letter+lower_letter
ID=digits+letter

libs=[]

id=[]
num=[]
token=[]

with open('source.txt','r') as f:
    texts=f.readlines()
    for text in texts:
        libs=libs+text.split()
# print(libs)
result=[]
for word in libs:
    print(word)
    if word in keyword.keys():
        result.append("("+str(keyword[word])+","+word+")")
        token.append(word)
    elif word in operator.keys():
        result.append("("+str(operator[word])+","+word+")")
        token.append(word)
    elif word.isdigit():
        result.append("(11,"+word+")")
        num.append(word)

    else:
        if word[0] in letter:
            for i in range(1,len(word)):
                if word[i] in ID:
                    continue
                else:
                    print("非法输入！这不是ID！")
                    break
            id.append(word)
            result.append("(10,"+word+")")

print(libs)
print(result)


