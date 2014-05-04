from exam_problem3 import *

def test_rabbit_growth():
    for i in range(15):
        rabbitGrowth()

def test_fox_growth():
    for i in range(15):
        foxGrowth()

def test_run_simulation():
    result = runSimulation(200)
    # for step in range(len(result[0])):
        # print(result[0][step], result[1][step])
    rabbitPopulationOverTime = result[0]
    foxPopulationOverTime = result[1]
    # pylab.plot(rabbitPopulationOverTime, label = 'Rabbits')
    # # # pylab.show()
    # pylab.plot(foxPopulationOverTime, label = 'Foxes')
    # pylab.show()
    rabbit_coeff = pylab.polyfit(range(len(rabbitPopulationOverTime)), rabbitPopulationOverTime, 2)
    pylab.plot(pylab.polyval(rabbit_coeff, range(len(rabbitPopulationOverTime))))
    # pylab.show()

    fox_coeff = pylab.polyfit(range(len(foxPopulationOverTime)), foxPopulationOverTime, 2)
    pylab.plot(pylab.polyval(fox_coeff, range(len(foxPopulationOverTime))))
    pylab.show()

# test_rabbit_growth()
# test_fox_growth()
test_run_simulation()