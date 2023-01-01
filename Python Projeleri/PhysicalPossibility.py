# bu projede fizik dersinde ki olasılık hesaplamalarını yapacağız. 

import random
import math

def throwNeedles(numNeedles):
    inCircle = 0
    for Needles in range(1, numNeedles + 1):
        x = random.random()
        y = random.random()
        distance = math.sqrt(x**2 + y**2)
        if distance <= 1:
            inCircle += 1
    return (4 * (inCircle / float(numNeedles)))

def getEst(numNeedles, numTrials):
    estimates = []
    for t in range(numTrials):
        piGuess = throwNeedles(numNeedles)
        estimates.append(piGuess)
    sDev = stdDev(estimates)
    curEst = sum(estimates) / len(estimates)
    print('Est. = ' + str(curEst) + ', Std. dev. = ' + str(round(sDev, 6)) + ', Needles = ' + str(numNeedles))
    return (curEst, sDev)

def stdDev(X):
    mean = sum(X) / len(X)
    tot = 0.0
    for x in X:
        tot += (x - mean) ** 2
    return math.sqrt(tot / len(X))

def estPi(precision, numTrials):
    numNeedles = 1000
    sDev = precision
    while sDev >= precision / 1.96:
        curEst, sDev = getEst(numNeedles, numTrials)
        numNeedles *= 2
    return curEst

estPi(0.005, 100)

