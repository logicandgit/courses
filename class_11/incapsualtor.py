# -*- coding: utf-8 -*- 
class JustCounter(object):
    __secretCount = 0

    def count(self):
        self.__secretCount += 1
        print self.__secretCount
