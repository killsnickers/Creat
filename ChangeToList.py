# -*- coding: utf-8 -*-
fo = open("foo.txt", "r")
fy = open("StationList.py", "w")
res = []
for i in fo.readlines():
    print i
    res.append('u\''+i.strip()+'\',')
n = 0
for i in res:
    n+=1
    fy.write(i)
    if n%10 == 0:
        fy.write('\n')
fo.close()
fy.close()