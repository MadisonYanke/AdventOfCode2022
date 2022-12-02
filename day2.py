import time
startTime = time.time()


####
lines = open("./day2", "r").read().splitlines()
def calcScore(me, opp):
    if (me == opp): return 3
    elif (me == "A" and opp == "C"): return 6
    elif (me == "C" and opp == "A"): return 0
    elif (me > opp): return 6
    elif (opp > me): return 0
def calcSymbol(outcome, opp):
    if (outcome == "Y"):
        if (opp == "A"): return "X"
        elif (opp == "B"): return "Y"
        elif (opp == "C"): return "Z"
    elif (outcome == "X"):
        if (opp == "A"): return "Z"
        elif (opp == "B"): return "X"
        elif (opp == "C"): return "Y"
    elif (outcome == "Z"):
        if (opp == "A"): return "Y"
        elif (opp == "B"): return "Z"
        elif (opp == "C"): return "X"

def runRounds(input, calcSymbolFlag):
    totalScore = 0
    for line in input:
        roundScore = 0
        opponent = line.split()[0]
        mySymbol = calcSymbol(line.split()[1], opponent) if calcSymbolFlag else line.split()[1]
        match mySymbol:
            case "X":
                roundScore += 1
                roundScore += calcScore("A", opponent)
            case "Y":
                roundScore += 2
                roundScore += calcScore("B", opponent)
            case "Z":
                roundScore += 3
                roundScore += calcScore("C", opponent)
        totalScore += roundScore
    return totalScore
print("pt1", runRounds(lines, False))
print("pt2", runRounds(lines, True))
####


executionTime = (time.time() - startTime)
print("Execution time (ms): " + str(executionTime * 1000))