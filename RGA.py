#!/usr/bin/python
# -*- coding: utf-8 -*-

from numpy import *
import random

#############################################<Fitness function chromosome>##############################################
#здесь описаны фитнес функции
class Fitness:
    def __init__ (self):pass
    def __call__(self,value):pass

class FitnessFunction (Fitness):
    def __call__(self,value):
        self.__value = value
        return 2 * pow(self.__value,2) + 1
########################################################################################################################

#############################################<Selection <Method Rullet> >###############################################
#селекция хромосомы "Метод рулетки"    

class Selector:
    def __init__(self): pass
    def __call__(self,pop): pass

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
########################################################################################################################

#############################################<Crossover>################################################################
#реализация кроссинговера: "Арифметический кроссовер"    
class Crossover:
    def __init__(self):pass
    def __call__(self,population):pass

class ArithmeticalCrossover(Crossover):
    def init(self,kinder,alpha,teta):
        self.kinder = kinder
        self.alpha = alpha
        self.teta = teta
    # kinder = eltern2 * alpha - eltern2 * (1 - alpha)//eltern - родитель
    def __call__(self,population):
        self.population = population
        self.kinder = zeros((6,1))#primer
        self.alpha = random.uniform(0.5,0.9)
        self.teta = (1 - self.alpha)

        for i in xrange(len(self.kinder)):
            self.kinder = self.population * self.alpha - self.population * self.teta
        return self.kinder

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
    
########################################################################################################################

#############################################<Mutator Chromosome>#######################################################
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
        self.random_value = random.uniform(self.range_mutation_population_min,self.range_mutation_population_max)#итервал от мин. до макс.
        return self.random_value
    
########################################################################################################################

##########################################<Funnction minimum and maximum value>#########################################
#фу-ии для нахождения минимума или максимума в массиве.
class MinFun:
    def __init__(self):pass
    def __call__(self,Array):pass
    
class MaxFun:
    def __init__(self):pass
    def __call__(self,ArrayMax):pass

class MinimumValue(MinFun):
    def __call__(self,Array):
        self.Array = Array
        self.Minimum = self.Array[0]
        self.N = len(self.Array)

        for i in xrange(self.N):
            if self.Array[i] < self.Minimum:
                self.Minimum = self.Array[i]
        return self.Minimum

class MaximumValue(MaxFun):
    def __call__(self,ArrayMax):
        self.ArrayMax = ArrayMax
        self.Maximum = self.ArrayMax[0]
        self.N = len(self.ArrayMax)

        for i in xrange(self.N):
            if self.ArrayMax[i] > self.Maximum:
                self.Maximum = self.ArrayMax[i]
        return self.Maximum
    
########################################################################################################################

####################################<Main Real-Coded Genetic Algorithm>#################################################
#реализация вещ. ген. алг. с применением всех созданных классов.    
class RCGA:
    def __init__(self): pass
    def __call__(self,ArrayData,Rate): pass

class RealCodedGeneticAlgorithm(RCGA):
    def _init_(self,_Selector_M_Roulette,_Function,_ArithmeticCrossover,_MutatorRandom,_MinimumValue,_MaximumValue):
        self._Selector_M_Roulette = Selector_M_Roulette
        self._Function = _Function# fitness function
        self._ArithmeticCrossover = _ArithmeticCrossover
        self._MutatorRandom = _MutatorRandom  
        self._MinimumValue = _MinimumValue
        #self.MaximumValue = MaximumValue

    def __call__(self,ArrayData,Rate):
        self.Rate = Rate #percent
        self.ArrayData = ArrayData

        self._MaximumValue1 = 10.001#size minimuma for values 
        self._Selector_M_Roulette = MethodRoulette()
        self._Function = FitnessFunction()
        self._ArithmeticCrossover = ArithmeticalCrossover()
        self._MutatorRandom = RandomMutator()
        self._MinimumValue = MinimumValue()
        #self.MaximumValue = MaximumValue()

        for i in xrange(len(self.ArrayData)):
            self.Fun = self._Function(self.ArrayData)
            self.Select = self._Selector_M_Roulette(self.Fun)
            self.Cross = self._ArithmeticCrossover(self.Select)
            self.Mut = self._MutatorRandom(self.Cross,self.Rate)
            if self._MinimumValue(self.Mut) < self._MaximumValue1:
                self._CreateNewPopulation = self.Mut
            else:
                self._BestPopulation = self._CreateNewPopulation
        return self._CreateNewPopulation
    
#----------------------------------------------------------------------------------------------------------------------#        
from numpy import random

def TestPrint():
    DATA = random.random_sample([25,1]) * 10.
    _RGA_ = RealCodedGeneticAlgorithm()
    MIN_VALUE = MinimumValue()
    _FitnessFunction = FitnessFunction()
    
    Step = 25
    print "Started data::",'\n',DATA,'\n'    
    print "Real-Coded Genetic Algorithm::"
    for i in xrange(Step):
        rga = _RGA_(DATA,0.01)#0.01 -> rate == 10%
        minrezult = MIN_VALUE(rga)
        print rga,'\n',"The minimum value at each sten RGA::",minrezult,'\n'
    return rga, minrezult
    
#----------------------------------------------------------------------------------------------------------------------#    
if __name__=='__main__':
    TestPrint()
#--------<<~!@CrOcOdIlUs@!~>>--------#
