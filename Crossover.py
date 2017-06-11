#!/usr/bin/python
# -*- coding: utf-8 -*-

from numpy import *
import random

class Crossover:
    def __init__(self):pass
    def __call__(self,population):pass
# арифметический оператор скрещивания
class ArithmeticalCrossover(Crossover):
    def init(self,kinder,alpha,teta):
        self.kinder = kinder
        self.alpha = alpha
        self.teta = teta
    # kinder = eltern2 * alpha - eltern2 * (1 - alpha)//eltern - родитель
    def __call__(self,population):
        self.population = population # популяция хромосом
        self.kinder = zeros((6,1))#результат при скрещивании двух особей (детище!)
        self.alpha = random.uniform(0.5,0.9)
        self.teta = (1 - self.alpha)

        for i in xrange(len(self.kinder)):
            self.kinder = self.population * self.alpha - self.population * self.teta
        return self.kinder
# BLX-a скрещивание хромосом
class BlxAlpha(Crossover):
    def __call__(self,population):
        self.population = population 
        self.MIN_VAL = MinimumValue()
        self.MAX_VAL = MaximumValue()
        self.alpha = 0.5
        self.KinderPopulation = zeros((6,1))
        
        for i in xrange(len(self.KinderPopulation)):
            self.min = self.MIN_VAL(self.population)
            self.max = self.MAX_VAL(self.population)
            self.I = self.max - self.min
            self.KinderPopulation = random.uniform (self.min - self.I * self.alpha,self.max + self.I * self.alpha)
        return self.KinderPopulation
    
