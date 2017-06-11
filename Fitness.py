#!/usr/bin/python
# -*- coding: utf-8 -*-

from numpy import *

class Fit:
    def __init__ (self):pass
    def __call__(self,value):pass

class Fitness (Fit):
    def __call__(self,value):
        self.__value = value
        return 2 * pow(self.__value,2) + 1

def Test():
    fit = Fitness()

    arr = array([[2.34,3.54,4.342,5.098,6.987]])

    for i in xrange(len(arr)):
        print fit(arr)

if __name__=='__main__':
    Test()
        
    
