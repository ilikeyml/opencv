import ClassifyTree as ct
import math
myData, lables = ct.createDataset()
shannonEnt = ct.calcShannonEnt(myData)
print 'ShannonEnt:%s' %shannonEnt
myData[0][-1] = 'maybe'
shannonEnt = ct.calcShannonEnt(myData)
print 'ShannonEnt:%s' %shannonEnt
