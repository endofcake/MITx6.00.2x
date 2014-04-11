from ps3b import *

numViruses = 100
maxPop = 1000
maxBirthProb = 0.99
clearProb = 0.05
numTrials = 30

mutProb = 0.5
popDensity = 0.1

def test_simple_virus():
	simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb, numTrials)

def test_resistant_virus():
	resistances = {'guttagonol':False, 'srinol':False}
	active_drugs = {'guttagonol':False, 'srinol':True}

	virii = [ResistantVirus(maxBirthProb, clearProb, resistances, mutProb) for i in range(10)]

	for i in range(3):
		for vir in virii:
			try:
				v = vir.reproduce(popDensity, active_drugs)
				print(v.getResistances())
			except NoChildException:
				pass


test_resistant_virus()