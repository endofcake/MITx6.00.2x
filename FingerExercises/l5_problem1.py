import random

def pickBall(bucket):
    random.shuffle(bucket)
    choice = bucket.pop()
    return choice

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    counter = 0

    for i in range(numTrials):
        bucket = [0, 0, 0, 1, 1, 1]
        chosen = [pickBall(bucket)]

        for j in range(2):
            chosen.append(pickBall(bucket))

        if sum(chosen) == 0 or sum(chosen) == 3:
            counter += 1

    return float(counter) / numTrials

print(noReplacementSimulation(10000))














    








