import time
startTime = time.time()
#####
lines = open("./day4", "r").read().splitlines()

containedAssignments, overlappingAssignments = 0, 0
for line in lines:
    a1raw, a2raw = line.split(',')[0], line.split(',')[1]
    assignment1 = set(range(int(a1raw.split('-')[0]), int(a1raw.split('-')[1])+1))
    assignment2 = set(range(int(a2raw.split('-')[0]), int(a2raw.split('-')[1])+1)) 
    if (assignment1.issubset(assignment2) or assignment2.issubset(assignment1)): containedAssignments += 1
    if (len(assignment1 & assignment2) != 0): overlappingAssignments += 1

print("pt1: ", containedAssignments, "pt2: ", overlappingAssignments)
####
executionTime = (time.time() - startTime)
print("Execution time (ms): " + str(executionTime * 1000))