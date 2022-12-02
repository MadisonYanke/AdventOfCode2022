import time
startTime = time.time()


####
rps = ["A", "B", "C"]
lines = open("./day2", "r").read().replace("X", "A").replace("Y", "B").replace("Z", "C").splitlines()
def calcScore(me, opp):
    if (rps.index(me) == rps.index(opp)): return 3
    elif ((rps.index(me)-1)%3 == rps.index(opp)): return 6
    elif ((rps.index(me)+1)%3 == rps.index(opp)): return 0
def calcSymbol(outcome, opp):
    if (outcome == "A"): return rps[(rps.index(opp)-1)%3]
    elif (outcome == "B"): return opp
    elif (outcome == "C"): return rps[(rps.index(opp)+1)%3]
def runRounds(input, calcSymbolFlag):
    totalScore = 0
    for line in input:
        opponent = line.split()[0]
        mySymbol = calcSymbol(line.split()[1], opponent) if calcSymbolFlag else line.split()[1]
        if (mySymbol == "A"): totalScore += 1 + calcScore("A", opponent)
        if (mySymbol == "B"): totalScore += 2 + calcScore("B", opponent)
        if (mySymbol == "C"): totalScore += 3 + calcScore("C", opponent)
    return totalScore
print("pt1", runRounds(lines, False))
print("pt2", runRounds(lines, True))
####


executionTime = (time.time() - startTime)
print("Execution time (ms): " + str(executionTime * 1000))