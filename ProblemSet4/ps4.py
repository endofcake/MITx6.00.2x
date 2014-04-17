# 6.00.2x Problem Set 4

import numpy
import random
import pylab
from ps3b import *

#
# PROBLEM 1
#      
def infect(numViruses, maxBirthProb, clearProb, resistances, mutProb):
    viruses = []
    for i in range(numViruses):
        viruses.append(ResistantVirus(maxBirthProb, clearProb,\
            resistances, mutProb))
    return viruses

def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    #delay_list = [300, 150, 75, 0]
    delay_list = [150]
    additional_steps = 150
    stat_dict = {}

    #predefined parameters
    numViruses = 100
    maxPop = 1000
    maxBirthProb = 0.1
    clearProb = 0.05
    resistances = {'guttagonol': False, 'grimpex': False}
    mutProb = 0.005

    for delay in delay_list:
        steps = delay + additional_steps
        virus_stats = [0 for x in range(steps)]
        viruses = infect(numViruses, maxBirthProb, clearProb, resistances, mutProb)
        stat_dict[delay] = []
        result = []

        for i in range(numTrials):
            p = TreatedPatient(viruses, maxPop)
            round = 0

            while round < delay:
                p.update()
                round += 1

            p.addPrescription('guttagonol')
            while round < steps:
                p.update()
                round += 1

            final_pop = p.getTotalPop()
            result.append(final_pop)
        print('Finished calculating delay ' + str(delay))
        plot_histogram(result, delay)

def plot_histogram(data, delay):        
    #data = pylab.array(data)
    print(data)
    pylab.hist(data, bins=51)
    pylab.title('Mean virus population, delay ' + str(delay))
    pylab.xlabel('Elapsed time steps')
    pylab.ylabel('Average size of the virus population in the patient')
    #pylab.legend(loc = 'lower right')
    pylab.show()
    #return stat_dict






#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    delay_list = [300, 150, 75, 0]
    #delay_list = [150]
    additional_steps = 150
    stat_dict = {}

    #predefined parameters
    numViruses = 100
    maxPop = 1000
    maxBirthProb = 0.1
    clearProb = 0.05
    resistances = {'guttagonol': False, 'grimpex': False}
    mutProb = 0.005

    for delay in delay_list:
        first_drug = delay + additional_steps
        second_drug = first_drug + additional_steps
        #virus_stats = [0 for x in range(steps)]
        viruses = infect(numViruses, maxBirthProb, clearProb, resistances, mutProb)
        #stat_dict[delay] = []
        result = []

        for i in range(numTrials):
            p = TreatedPatient(viruses, maxPop)
            round = 0

            while round < additional_steps:
                p.update()
                round += 1

            p.addPrescription('guttagonol')
            while round < first_drug:
                p.update()
                round += 1

            p.addPrescription('grimpex')
            while round < second_drug:
                p.update()
                round += 1

            final_pop = p.getTotalPop()
            result.append(final_pop)
        print('Finished calculating delay ' + str(delay))
        plot_histogram(result, delay)
