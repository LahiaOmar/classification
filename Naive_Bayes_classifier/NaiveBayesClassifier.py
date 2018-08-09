# let coding = begin

from math import sqrt, exp, pi, pow

class NaiveBayesClassifier:
  def __init__(self, dataSet):
    self.dataSet = dataSet
    self.size = len(dataSet)
    self.mapping = {}
    self.learningValues = {}
    self.createMatrix()

  def createMatrix(self):
    self.mappingClass()
    self.EVofClasses()
  
  def EVofClasses(self):
    for key, value in self.mapping.items():
      esps, vars = self.calculeEV(value)
      self.learningValues[ key ] = [esps , vars]
      print("esps of {0} : {1} and vars of {2} : {3}".format(key,esps,key,vars))
    
  def calculeEV(self, value):
    espOfParam = []
    varOfParam = []
    si = len(value)
    for i in range( len( value[0] ) ):
      sum = 0
      for j in range( si ):
         sum += value[j][i]
      espOfParam.append(sum/si)
      esp = sum/si
      sum = 0
      for j in range( si ):
        sum +=( ( value[j][i] - esp ) * ( value[j][i] - esp ) )
      if si != 1 : 
        varOfParam.append(sum/(si-1))
      else :
        varOfParam.append(sum)
    return espOfParam,varOfParam

  def LoiNormal(self, esp, var, value):
    return ( ( 1.0/(var*sqrt(2*pi)) )*( exp( (-1/2)*( pow( ( (value - var)/ var) ,2) ) ) ) )

  def mappingClass(self):
    indColumnClasses = len(self.dataSet[0]) -1
    for i in range(self.size):
      clsName = self.dataSet[i][indColumnClasses]
      row = self.dataSet[i]
      if clsName not in self.mapping:
        self.mapping[ clsName ] = []
        self.mapping[ clsName ].append(row[0: indColumnClasses])
      else:
        self.mapping[ clsName ].append(row[0: indColumnClasses]) 
    
  def caluclePredection(self, row):
    maxProbability = -1
    classMaxProbability = 'inconnu'
    for key, value in self.learningValues.items():
      sum = 1.0 / len(self.learningValues)
      for j in range( len( row ) ):
        sum *= self.LoiNormal(value[0][j], value[1][j], row[j])
      cur = self.min(sum, maxProbability, key, classMaxProbability)
      if cur != classMaxProbability:
        maxProbability = sum
        classMaxProbability = cur
    return classMaxProbability

  def min(self, a, b, newClassName, className):
    if a <=b :
      return className
    else:
      return newClassName

  def pridection(self, test):
    lastInd = len( test[0] ) -1
    for i in range( len( test ) ):
      row = test[i]
      predectClass = self.caluclePredection(row)
      print("for input = {0} prediction class is : {1}".format(row, predectClass))

