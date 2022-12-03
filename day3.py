import time
startTime = time.time()
#####

lines = open("./day3", "r").read().splitlines()

def findScore(char):
    if char.islower(): return ord(char) - 96
    else: return ord(char) - 38

totalPrio = 0
for line in lines:
    firstpart, secondpart = line[:len(line)//2], line[len(line)//2:]
    sameChar = list(set(firstpart) & set(secondpart))[0]
    totalPrio += findScore(sameChar)

print("pt1", totalPrio)
totalPrio = 0
for index in range(2, len(lines), 3):
    firstSack, secondSack, thirdSack = lines[index], lines[index-1], lines[index-2]
    sameChar = list(set(firstSack) & set(secondSack) & set(thirdSack))[0]
    totalPrio += findScore(sameChar)

print("pt2", totalPrio)

####
executionTime = (time.time() - startTime)
print("Execution time (ms): " + str(executionTime * 1000))