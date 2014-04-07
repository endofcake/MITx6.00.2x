import pylab

def sampleQuizzes():
    midterm1 = []
    midterm2 = []
    final = []

    for i in range(31):
    	midterm1.append(50 + i)
    	midterm2.append(60 + i)

    for i in range(41):
    	final.append(55 + i)

    

    results = []
    for z in range(10001):
    	import random
    	mid1 = random.choice(midterm1)
    	mid2 = random.choice(midterm2)
    	fin = random.choice(final)

    	total = calculate_grade(mid1, mid2, fin)

    	if total >= 70 and total <= 75:
    		results.append(1)

    return (len(results) * 1.0) / 10000.0

def calculate_grade(mid1, mid2, fin):
    	return mid1 * 0.25 + mid2 * 0.25 + fin * 0.5

def generateScores(numTrials):
    """
    Runs numTrials trials of score-generation for each of
    three exams (Midterm 1, Midterm 2, and Final Exam).
    Generates uniformly distributed scores for each of 
    the three exams, then calculates the final score and
    appends it to a list of scores.
    
    Returns: A list of numTrials scores.
    """
    midterm1 = []
    midterm2 = []
    final = []

    for i in range(31):
    	midterm1.append(50 + i)
    	midterm2.append(60 + i)

    for i in range(41):
    	final.append(55 + i)

    results = []
    for z in range(10001):
    	import random
    	mid1 = random.choice(midterm1)
    	mid2 = random.choice(midterm2)
    	fin = random.choice(final)

    	total = calculate_grade(mid1, mid2, fin)

    	results.append(total)
    return results

def plotQuizzes():
    results = generateScores(10000)    
    #xmin, xmax = pylab.xlim()
    #ymin, ymax = pylab.ylim()
    #pylab.figure()
    pylab.hist(results, bins = 7)
    #pylab.xlim(-1.0, 2.0)
    pylab.xlabel('Final score')
    pylab.ylabel('Number of Trials')
    pylab.title('Distribution of scores')
    #pylab.legend()
    pylab.show()

plotQuizzes()