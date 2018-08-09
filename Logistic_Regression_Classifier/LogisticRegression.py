# let coding = begin

from random import random
from math import exp
class LogisticRegression:
  def __init__(self, dataSet = [], learningRate = 0.2, it_max=1):
    self.dataSet = dataSet
    self.column = len(dataSet[0])
    self.row = len(dataSet)
    self.learningRate = learningRate
    self.it_max = it_max
    self.w = []
    self.init_weight()
    self.start_learning()
  
  def init_weight(self):
    """
      init weight of classifer, with random value.
    """
    for i in range(self.column - 1):
      self.w.append(random())
  
  def start_learning(self):
    it = 0
    while it<self.it_max:
      for i in range( self.column-1 ):
        deriv = self.derivation(i)
        self.w[i] += ( self.learningRate * ( deriv ) )
      it += 1

  def derivation(self, index):
    sum = 0.0
    indOfoutput = self.column-1
    for i in range(self.row):
      sum += ( self.dataSet[i][index] * ( self.dataSet[i][indOfoutput]  - self.probability(i)) )
    return sum

  def getSum(self, index):
    sum = 0.0
    for i in range(self.column-1):
      sum += ( self.w[i] * self.dataSet[index][i] )
    return sum 
  
  def probability(self, index):
    sumOfWeight = self.getSum(index) 
    return self.sigmoid(sumOfWeight)

  def sigmoid(self,x):
    return (1.0/( 1.0 + exp(-x/10000)))
  def prediction(self, test):
    for i in range(len(test)):
      sum = 0.0
      for j in range(self.column-1):
        sum += ( self.w[i] * test[i][j] )
      print("input = {0} prediction : {1} ".format(test[i],self.sigmoid(sum)))

  def printWeight(self):
    out = []
    for i in range(self.column -1):
      out.append(self.w[i])