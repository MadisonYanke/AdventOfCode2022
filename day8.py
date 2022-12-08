import time
import math
startTime = time.time()
#####
lines = open("./day8", "r").read().splitlines()

trees = []

for line in lines:
    trees.append(list(line))

visibleTrees = set()
for row in range(len(trees)):
    currentHeight = 0
    #left check
    for col in range(len(trees[row])):
        if col == 0:
            visibleTrees.add(str(row).zfill(3) + str(col).zfill(3))
            currentHeight = trees[row][col]
        else:
            if trees[row][col] > currentHeight:
                visibleTrees.add(str(row).zfill(3) + str(col).zfill(3))
                currentHeight = trees[row][col]
        if currentHeight == 9:
            break
    #right check
    for colF in range(len(trees[row])):
        col = len(trees)-(colF) - 1
        if col == len(trees)-1:
            visibleTrees.add(str(row).zfill(3) + str(col).zfill(3))
            currentHeight = trees[row][col]
        else:
            if trees[row][col] > currentHeight:
                visibleTrees.add(str(row).zfill(3) + str(col).zfill(3))
                currentHeight = trees[row][col]
        if currentHeight == 9:
            break
    
for col in range(len(trees[0])):
    currentHeight = 0
    #up check
    for row in range(len(trees)):
        if row == 0:
            visibleTrees.add(str(row).zfill(3) + str(col).zfill(3))
            currentHeight = trees[row][col]
        else:
            if trees[row][col] > currentHeight:
                visibleTrees.add(str(row).zfill(3) + str(col).zfill(3))
                currentHeight = trees[row][col]
        if currentHeight == 9:
            break
    #down check
    for rowF in range(len(trees)):
        row = len(trees)-(rowF) - 1
        if row == len(trees)-1:
            visibleTrees.add(str(row).zfill(3) + str(col).zfill(3))
            currentHeight = trees[row][col]
        else:
            if trees[row][col] > currentHeight:
                visibleTrees.add(str(row).zfill(3) + str(col).zfill(3))
                currentHeight = trees[row][col]
        if currentHeight == 9:
            break

highestScenicScore = 0
for row in range(len(trees)):
    for col in range(len(trees[row])):
        scenicScores = [0,0,0,0]
        #check left
        for checkColF in range(col):
            checkCol = col-checkColF-1
            if trees[row][checkCol] < trees[row][col]:
                scenicScores[0] += 1
            else:
                scenicScores[0] += 1
                break
        #check right
        for checkCol in range(col + 1, len(trees[row])):
            if col == len(trees[row]) - 1:
                break
            if trees[row][checkCol] < trees[row][col]:
                scenicScores[1] += 1
            else:
                scenicScores[1] += 1
                break
        #check up
        for checkRowF in range(row):
            checkRow = row-checkRowF-1
            if trees[checkRow][col] < trees[row][col]:
                scenicScores[2] += 1
            else:
                scenicScores[2] += 1
                break
        #check down
        for checkRow in range(row + 1, len(trees)):
            if row == len(trees) - 1:
                break
            if trees[checkRow][col] < trees[row][col]:
                scenicScores[3] += 1
            else:
                scenicScores[3] += 1
                break
        if math.prod(scenicScores) > highestScenicScore:
            highestScenicScore = math.prod(scenicScores)
print("pt1: ", len(visibleTrees), " pt2: ", highestScenicScore)
####
executionTime = (time.time() - startTime)
print("Execution time (ms): " + str(executionTime * 1000))