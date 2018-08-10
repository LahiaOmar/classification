# let coding = begin

from pandas import pandas
from random import shuffle
from K_Nearest_Neightbors import K_Nearest_Neightbors

def splitData(data):
  r = []
  end = len(data[0])
  for i in range(len(data)):
    for j in range(len(data[i])-1):
      data[i][j] = float(data[i][j])
  return data

dataSet = pandas.read_csv("../dataSet/iris.csv", sep=",").values
shuffle(dataSet)


data = splitData(dataSet[0:130])
test = splitData(dataSet[130:150])

knn = K_Nearest_Neightbors(dataSet=data,k=3)

knn.predection(test=test)