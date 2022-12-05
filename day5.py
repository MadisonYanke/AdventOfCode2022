
import copy
import time
startTime = time.time()
#####
lines = open("./day5", "r").read().splitlines()

stacks = [["S", "T", "H", "F", "W", "R"],
["S", "G", "D", "Q", "W"],
["B", "T", "W"],
["D", "R", "W", "T", "N", "Q", "Z", "J"],
["F", "B", "H", "G", "L", "V", "T", "Z"],
["L", "P", "T", "C", "V", "B", "S", "G"],
["Z", "B", "R", "T", "W", "G", "P"],
["N", "G", "M", "T", "C", "J", "R"],
["L", "G", "B", "W"]]

stacks2 = copy.deepcopy(stacks)

for line in lines:
    quantity, fromRow, toRow = int(line.split(' ')[1]), int(line.split(' ')[3]) - 1, int(line.split(' ')[5]) - 1
    for quant in range(0, quantity):
        stacks[toRow].append(stacks[fromRow].pop())

topStacks = ""
for stack in stacks:
    topStacks += stack[-1]
print(topStacks)

for line in lines:
    quantity, fromRow, toRow = int(line.split(' ')[1]), int(line.split(' ')[3]) - 1, int(line.split(' ')[5]) - 1
    stacks2[toRow].extend(stacks2[fromRow][(-1 * quantity):])
    del stacks2[fromRow][(-1 * quantity):]

topStacks = ""
for stack in stacks2:
    topStacks += stack[-1]
print(topStacks)
####
executionTime = (time.time() - startTime)
print("Execution time (ms): " + str(executionTime * 1000))