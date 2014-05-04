import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP

    # TO DO
    for rabbit in range(CURRENTRABBITPOP):
        birth_prob = 1.0 - (float(CURRENTRABBITPOP) / MAXRABBITPOP) 
        rand = random.random()
        if rand < birth_prob:
            if CURRENTRABBITPOP < MAXRABBITPOP:
                CURRENTRABBITPOP += 1
            else:
                break
            # print(rand, birth_prob)
    # print(CURRENTRABBITPOP)
            
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP

    # TO DO
    for fox in range(CURRENTFOXPOP):
        prob_eat_rabbit = (float(CURRENTRABBITPOP) / MAXRABBITPOP)
        luck = random.random()

        if luck < prob_eat_rabbit and CURRENTRABBITPOP > 10:
            CURRENTRABBITPOP -= 1 # eat it!
            if random.choice([1,2,3]) == 1: # 1/3 chance to reproduce
                CURRENTFOXPOP += 1
        else:
            die_chance = random.random()
            if die_chance < 0.9 and CURRENTFOXPOP > 10:
                CURRENTFOXPOP -= 1
        # print(CURRENTRABBITPOP, CURRENTFOXPOP)
    
            
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """

    # TO DO
    rabbit_populations = []
    fox_populations = []

    for step in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        rabbit_populations.append(CURRENTRABBITPOP)
        fox_populations.append(CURRENTFOXPOP)
    return (rabbit_populations, fox_populations)