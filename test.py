# -*- coding: utf-8 -*-


import creat
import datetime

class test():
    """n = 10000000
    m = 100000
    a = [1,2,3]
    a.reverse()
    print(a[0])
    dd = creat.creat()
    bit = dd.creatRandom(n, m)
    #dd.printAll(bit)
    starttime = datetime.datetime.now()
    result = []
    result = dd.inputNum(bit)
    result = dd.sort(n, m, result)
    for i in range(len(result)):
        print(result[i])
    endtime = datetime.datetime.now()
    print(endtime-starttime).seconds"""
    dd = creat.creat()
    a = u'(壹拾伍)'
    print dd.__trans__(a)
    print 1

    # 素数测试
    # 奇数生成
    def _odd_iter(self):
        n = 1
        while True:
            n = n + 2
            yield n

    def _not_division(self, n):

        return lambda x: x % n > 0

    def primes(self):
        yield 2
        it = self._odd_iter()
        while True:
            n = next(it)
            yield n
            it = filter(self._not_division(n), it)

    def tests(self):
        for n in self.primes():
            if n < 100:
                print n
            else:
                break
