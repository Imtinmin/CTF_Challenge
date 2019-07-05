# coding:UTF-8

global a
a="~}|{zyxwvutsrqponmlkjihgfedcba`_^]\[ZYXWVUTSRQPONMLKJIHGFEDCBA@?>"
# !!!!!!!! 字符串 a 可能不同,注意修改
b='DDCTF{reverseME}'
c=[]
for i in b:
    c.append(a.index(str(i))+32)
for i in c:
    print chr(i),