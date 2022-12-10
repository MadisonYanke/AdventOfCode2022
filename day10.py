import time
import math
startTime = time.time()
#####
lines = open("./day10", "r").read().splitlines()

value = 1

counter = 0
currenInst = 0
addingFlag = False
addingValue = 0
maxCycle = 240

renderer = ["", "", "", "", "", ""]

for currentCycle in range(1, maxCycle+1):
    
    
    if currentCycle in [20, 60, 100, 140, 180, 220]:
        counter += currentCycle * value

    if (value+1 - currentCycle%40 <= 1 and value+1 - currentCycle%40 >= -1):
        renderer[math.ceil(currentCycle/40) - 1] += "█"
    else:
        renderer[math.ceil(currentCycle/40) - 1] += " "

    if addingFlag:
        value += addingValue
        addingFlag = False
    else:
        inst1 = lines[currenInst].split(' ')[0]
        if inst1 == "addx":
            inst2 = lines[currenInst].split(' ')[1]
            addingValue = int(inst2)
            addingFlag = True
        currenInst += 1
    
    currentCycle += 1



print("pt1: ", counter)
for rend in renderer:
    print(rend)
####
executionTime = (time.time() - startTime)
print("Execution time (ms): " + str(executionTime * 1000))