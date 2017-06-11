#!/usr/bin/python
# -*- coding: utf-8 -*-

from numpy import *
import random

class Selector:
    def __init__(self): pass
    def __call__(self,pop): pass
#Метод колеса рулетки
class MethodRoulette(Selector):
    #ps(chi) = Fit(chi)/sum(F(chi)) - нахождение вероятности селекции хромосомы.
    def Ps(self,ch):
        self.ch = ch
        self.__sum = 0.0
        self.newarray = zeros((6,1))#primer
        self.fit = FitnessFunction()

        for i in xrange(len(self.newarray)):
            self.__sum += self.fit(self.ch[i])
            self.newarray = divide(self.fit(self.ch),self.__sum)
        return self.newarray
    #v(chi) = ps(chi) * 100 - находим сектор колеса рулетки.
    def __call__(self,pop):
        self.pop = pop
        self.Pi = MethodRoulette()
        self.newArrayVi = zeros((6,1))#primer

        for j in xrange(len(self.newArrayVi)):
            self.newArrayVi = multiply(self.Pi.Ps(self.pop),100)
        return self.newArrayVi
