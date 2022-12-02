import time
startTime = time.time()


####
import heapq

lines = open("./day1", "r").read().splitlines()

def GetTopXElfCalories(elfList, x):
    calories = []
    currentElfTotal = 0
    for line in elfList:
        if (line == ''):
            calories.append(currentElfTotal)
            currentElfTotal = 0
            continue
        else:
            currentElfTotal += int(line)

    topCalories = sum(heapq.nlargest(x, calories))
    print(topCalories)


GetTopXElfCalories(lines, 1)
GetTopXElfCalories(lines, 3)
####


executionTime = (time.time() - startTime)
print("Execution time (ms): " + str(executionTime * 1000))