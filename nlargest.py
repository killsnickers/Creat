# -*- encoding: utf-8 -*-

import heapq

num = [1,2,3,5,6,3,786,4,3,23,233,87]
q = list(num)
heapq.heapify(q)
print heapq.heappop(q)
print q
e = (2,3)
c = (1,9)
print e>c
