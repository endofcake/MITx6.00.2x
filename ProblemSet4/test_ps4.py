from ps4 import *

def test_simulation_delay():
	result = simulationDelayedTreatment(500)
	#print(result)

def test_drugs_cocktail():
	result = simulationTwoDrugsDelayedTreatment(500)
	print(result)

#test_simulation_delay()
test_drugs_cocktail()
