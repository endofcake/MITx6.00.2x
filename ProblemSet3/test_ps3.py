from ps3b import *

numViruses = 100
maxPop = 1000
maxBirthProb = 0.99
clearProb = 0.05
numTrials = 10

mutProb = 0.5
popDensity = 0.1

resistances = {'guttagonol':True, 'srinol':False}
active_drugs = {'guttagonol':True, 'srinol':False}

def test_simple_virus():
	simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb, numTrials)

def test_resistant_virus():
	virii = [ResistantVirus(maxBirthProb,\
	clearProb, resistances, mutProb) for i in range(10)]

	for i in range(3):
		print("Round ", i, )
		for vir in virii:
			try:
				v = vir.reproduce(popDensity, active_drugs)
				print(v.getResistances())
			except NoChildException:
				pass

def test_positive_mutability():
	virus = ResistantVirus(1.0, 0.0, {"drug2": True}, 1.0)
	child = virus.reproduce(0, ["drug2"])
	for i in range(10):
		print(virus.reproduce(0, []).getResistances())

def test_mutability():
	virus = ResistantVirus(1.0, 0.0, {'drug1':True, 'drug2': True,\
	 'drug3': True, 'drug4': True, 'drug5': True, 'drug6': True}, 0.5)

	for i in range(10):
		print(virus.reproduce(0, []).getResistances())

def test_negative_mutability():
	virus = ResistantVirus(1.0, 0.0, {"drug1": True}, 0.0)

	for i in range(10):
		print(virus.reproduce(0, []).getResistances())

def test_treated_patient():
	virii = [ResistantVirus(maxBirthProb,\
	 clearProb, resistances, mutProb) for i in range(10)]
	p = TreatedPatient(virii, 100)
	p.addPrescription('guttagonol')
	print(p.getResistPop(p.getPrescriptions()))

	p.addPrescription('srinol')
	print(p.getResistPop(p.getPrescriptions()))

	p.update()

def test_untreatable_patient():
	virus = ResistantVirus(1.0, 0.0, {}, 0.0)
	patient = TreatedPatient([virus], 100)

	for i in range(10):
		print(i)
		patient.update()

	print(patient.getResistPop(patient.getPrescriptions()))

def test_simulation_drug():
	processed_reg, processed_resist = simulationWithDrug(numViruses, maxPop, maxBirthProb, \
		clearProb, resistances, mutProb, numTrials)

	print(processed_reg, processed_resist)
#test_negative_mutability()
#test_positive_mutability()
#test_treated_patient()
#test_untreatable_patient()
test_simulation_drug()

