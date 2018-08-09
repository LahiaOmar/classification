# let coding = begin

from LogisticRegression import LogisticRegression 

dataSet = [
  [182, 81.6, 30, 0],
  [180, 86.2, 28, 0],
  [170, 77.1, 30, 0],
  [180, 74.8, 25, 0],
  [152, 45.4, 15, 1],
  [168, 68.0, 20, 1],
  [165, 59.0, 18, 1],
  [165, 59.0, 23, 1]
]

test =  [
  [183,59,20]
]

logit = LogisticRegression(dataSet,learningRate=0.1,it_max=100)

logit.prediction(test)