# -*- coding: utf-8 -*-
#迭代转进制
def test(x,y):
   if x!=0:
       test(x/y,y)
       print(x%y)

def test1(x,y):
    tmp_int=x
    tmp_list=[]
    while 1:
        tmp_list.append(str(tmp_int % y))
        tmp_int=tmp_int/y
        if tmp_int == 0:
            break
    tmp_list.reverse()
    return int("".join(tmp_list))
test(193,2)
print(test1(193,2))