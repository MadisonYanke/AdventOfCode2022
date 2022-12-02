import time
startTime = time.time()


####
rps = ["A", "B", "C"]
lines = open("./day2", "r").read().replace("X", "A").replace("Y", "B").replace("Z", "C").splitlines()
def calcScore(me, opp):
    return (3 if (rps.index(me) == rps.index(opp)) else 6 if (rps.index(me)-1)%3 == rps.index(opp) else 0)
def calcSymbol(outcome, opp):
    return (rps[(rps.index(opp)-1)%3] if (outcome == "A") else rps[(rps.index(opp)+1)%3] if (outcome == "C") else opp)
def runRounds(input, calcSymbolFlag):
    totalScore = 0
    for line in input:
        mySymbol = calcSymbol(line.split()[1], line.split()[0]) if calcSymbolFlag else line.split()[1]
        totalScore += (1 + calcScore("A", line.split()[0])) if (mySymbol == "A") else (2 + calcScore("B", line.split()[0])) if (mySymbol == "B") else (3 + calcScore("C", line.split()[0]))
    return totalScore
print("pt1", runRounds(lines, False), "pt2", runRounds(lines, True))
####


executionTime = (time.time() - startTime)
print("Execution time (ms): " + str(executionTime * 1000))