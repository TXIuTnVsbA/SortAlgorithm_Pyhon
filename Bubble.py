# -*- coding: utf-8 -*-
def BubbleSort(arg,log):
    tmp=list(arg)
    n = len(arg)
    flag = True
    if log != 0:
        print(arg)
        print(tmp)
    while (flag):
        flag=False
        for x in range(n):
            for y in range(x+1,n):
                if tmp[y-1] > tmp[y]:
                    i = tmp[y-1]
                    tmp[y-1]=tmp[y]
                    tmp[y] = i
                    if log != 0:
                        print(tmp)
                    flag=True
    return "".join(tmp)
print(BubbleSort("59238471",1))
