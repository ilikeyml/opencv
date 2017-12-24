import math
def calcShannonEnt(dataset):
     numEntries = len(dataset)
     #print numEntries
     labelCounts = {}
     for featVect in dataset:
         curVect = featVect[-1]
         if curVect not in labelCounts.keys():
             labelCounts[curVect] = 0
         labelCounts[curVect] += 1
     print 'LabelCounts:%s' %labelCounts
     shannonEnt = 0.0
     for key in labelCounts:
         #print labelCounts[key]
         prob = float(labelCounts[key]) / numEntries
         #print prob
         shannonEnt -= prob*math.log(prob, 2)
     return shannonEnt

def createDataset():
    dataset = [[1,1,'yes'],
               [1,1,'yes'],
               [1,0,'no'],
               [0,1,'no'],
               [0,1,'no']]
    labels = ['nosurfacing', 'flippers']
    return dataset, labels


