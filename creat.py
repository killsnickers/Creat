# -*- coding: utf-8 -*-

import random


class creat():
    def __init__(self):
        self.__WordsPatterns__ = (
            u'壹', u'贰', u'叁', u'肆', u'伍', u'陆', u'柒', u'捌', u'玖', u'零', u'拾', u'佰', u'仟', u'万', u'亿')
        self.__Suffix__ = (u'整', u'元', u'圆')
        self.__Num__ = {u'壹': 1, u'贰': 2, u'叁': 3,
                        u'肆': 4, u'伍': 5, u'陆': 6,
                        u'柒': 7, u'捌': 8, u'玖': 9,
                        u'零': 0}
        self.__Sit__ = {u'拾': 10, u'佰': 100, u'仟': 1000}
        self.__Large__ = {u'万': 10000,}
        self.__SuperLarge__ = {u'亿': 100000000}

    def creatRandom(self, n, m):
        bit = [0]*n
        for i in range(m):
            bit[i] = 1
        for i in range(n):
            bit = self.switchBit(i, int(random.random()*n), bit)
        return bit

    def switchBit(self, a, b, bit):
        c = bit[a]
        bit[a] = bit[b]
        bit[b] = c
        return bit

    def printAll(self, bit):
        for i in range(len(bit)):
            if bit[i] == 1:
                print(i)

    def inputNum(self, bit):
        #bit.reverse()
        result = []
        for i in range(len(bit)):
            if bit[i] == 1:
                result.append(i)
        result.reverse()
        #print result
        return result

    def sort(self, n, m, first):
        bit = [0]*n
        for i in range(len(first)):
            bit[first[i]] = 1
        result = self.outputNum(bit)
        return result

    def outputNum(self, bit):
        #bit = reversed(bit)
        result = []
        for i in range(len(bit)):
            if bit[i] == 1:
                result.append(i)
        return result


    def __trans__(self,  amout_words):
        number = 0
        current_number = 1
        if amout_words[0] not in self.__Num__ and amout_words[0] != u'拾':
            return 0
        for index in range(len(amout_words)):
            if self.__Num__.has_key(amout_words[index]):
                current_number = self.__Num__.get(amout_words[index])
            elif self.__Sit__.has_key(amout_words[index]):
                current_number = current_number*self.__Sit__.get(amout_words[index])
                number += current_number
                current_number = 0
            elif self.__Large__.has_key(amout_words[index]):
                number = number+current_number
                current_number = 0
                number = number*self.__Large__.get(amout_words[index])
            elif self.__SuperLarge__.has_key(amout_words[index]):
                number = number + current_number
                current_number = 0
                return number*self.__SuperLarge__.get(amout_words[index]) + self.__trans__(amout_words[index+1:])
            elif amout_words[index] in self.__Suffix__:
                number += current_number
                return number
            else:
                return 0
        number += current_number

        return number

    #素数测试
    #奇数生成
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

    def test(self):
        for n in self.primes():
            if n < 100:
                print n
            else:
                break