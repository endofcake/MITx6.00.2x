from ps3b import *

numViruses = 100
maxPop = 1000
maxBirthProb = 0.1
clearProb = 0.05
numTrials = 30

simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb, numTrials)

"""
for  i in range(0,10):
    p.update()
    print(i, p.getTotalPop())
    """