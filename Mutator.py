#!/usr/bin/python
# -*- coding: utf-8 -*-

from numpy import *
import random

#мутатор: используется случайная мутация.    
class Mutator:
    def __init__(self): pass
    def __call__(self,chromosome_value,rate): pass

class RandomMutator(Mutator):
    def __call__(self,chromosome_value,rate):
        self.chromosome_value = chromosome_value
        self.rate = rate
        self.new_mutation_population = zeros((6,1))
        self.range_mutation_population_min = self.chromosome_value - self.chromosome_value * self.rate#находим минимум
        self.range_mutation_population_max = self.chromosome_value + self.chromosome_value * self.rate#находим максимум
        self.random_value = random.uniform(self.range_mutation_population_min,self.range_mutation_population_max)#интервал от мин. до макс.
        return self.random_value
