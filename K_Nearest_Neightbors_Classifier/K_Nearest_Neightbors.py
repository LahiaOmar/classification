# let coding = begin

from math import fabs, sqrt, pow


class K_Nearest_Neightbors:
  def __init__(self, dataSet = [], k = 2, order = 2):
    self.dataSet = dataSet
    self.size = len( dataSet )
    self.column = len(dataSet[0])
    self.k = k
    self.order = order

  def distance(self, x, y):
    sum = 0.0
    for i in range(len(x)):
      sum += pow(fabs( x[i] - y[i] ), self.order)
    return pow(sum, 1.0/self.order)
  
  def getMost(self, row):
    mp = {}
    for i in range(len(row)):
      if row[i][1] not in mp:
        mp[row[i][1]] = 0
      mp[row[i][1]] += 1
    most = ''
    mx = -1
    for curMost, value in mp.items():
      most = self.min(mx, most, value, curMost)
    return most

  def min(self, mx, most, value, curMost):
    if value <= mx:
      return most
    return curMost
  def predection(self, test = []):
    for i in range(len( test )):
      distances = []
      cur_row_test = test[i][0:self.column-1]
      for j in range(self.size):
        cur = self.dataSet[j][0: self.column-1]
        dist = self.distance(cur_row_test, cur)
        distances.append((dist, self.dataSet[j][self.column-1]))
      distances.sort(key = lambda tup : tup[0])
      print("for this input {0} prediction is : {1} ".format(test[i], self.getMost(distances[0:self.k])))
      

  