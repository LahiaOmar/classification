# let coding = begin

from NaiveBayesClassifier import NaiveBayesClassifier
import pandas as pandas

dataSet = [
  [182, 81.6, 30, 'masculin'],
  [180, 86.2, 28, 'masculin'],
  [170, 77.1, 30, 'masculin'],
  [180, 74.8, 25, 'masculin'],
  [152, 45.4, 15, 'feminin'],
  [168, 68.0, 20, 'feminin'],
  [165, 59.0, 18, 'feminin'],
  [165, 59.0, 23, 'feminin']
]

test =  [
  [183,59,20]
]

nbc = NaiveBayesClassifier(dataSet)
nbc.pridection(test)