import time
startTime = time.time()
#####
lines = open("./day7", "r").read().splitlines()

root = {"/": {}}

workingDir = ["/"]

for line in lines:
    if line[0] == '$':
        cmd = line.split(' ')[1]
        if cmd == 'cd':
            wd = line.split(' ')[2]
            if wd == '/':
                workingDir = ['/']
            elif wd == '..':
                workingDir.pop()
            else:
                workingDir.append(wd)
    else:
        if line.split(' ')[0] == 'dir':
            currentObj = root
            for d in workingDir:
                currentObj = currentObj[d]
            currentObj[line.split(' ')[1]] = {}
        else:
            currentObj = root
            for d in workingDir:
                currentObj = currentObj[d]
            currentObj[line.split(' ')[1]] = line.split(' ')[0]


def findTotalSizeUnderThreshold(tree, totalSize, threshold):
    currentSize = 0
    for key in tree:
        if type(tree[key]) is dict:
            currentSize += findTotalSizeUnderThreshold(tree[key], totalSize, threshold)
        else:
            currentSize += int(tree[key])
    if currentSize <= threshold:
        totalSize["size"] += currentSize
    return currentSize

def findObjToDelete(tree, currentDeleteSize, targetDelete):
    currentSize = 0
    for key in tree:
        if type(tree[key]) is dict:
            currentSize += findObjToDelete(tree[key], currentDeleteSize, targetDelete)
        else:
            currentSize += int(tree[key])
    if currentSize < currentDeleteSize["size"] and currentSize > targetDelete:
        currentDeleteSize["size"] = currentSize
    return currentSize

totalSize = {"size": 0}
sizeUsed = findTotalSizeUnderThreshold(root, totalSize, 100000)
amountToDelete = 30000000 - (70000000 - sizeUsed)
delSize = {"size": sizeUsed}
findObjToDelete(root, delSize, amountToDelete)

print("pt1: ", totalSize["size"], "pt2: ", delSize["size"])
####
executionTime = (time.time() - startTime)
print("Execution time (ms): " + str(executionTime * 1000))