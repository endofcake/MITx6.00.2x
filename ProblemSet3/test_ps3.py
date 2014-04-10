from ps3b import *

numViruses = 1
maxPop = 100
maxBirthProb = 0.99
clearProb = 0.1
numTrials = 100

simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb, numTrials)

"""
for  i in range(0,10):
    p.update()
    print(i, p.getTotalPop())
    """