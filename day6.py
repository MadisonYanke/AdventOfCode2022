import time
startTime = time.time()
#####
datastream = open("./day6", "r").read()
def firstUniqueXLen(data, x):
    for n in range(x, len(data)):
        if len(set(data[n-x:n])) == x:
            return n
print("pt1: ", firstUniqueXLen(datastream, 4), " pt2: ", firstUniqueXLen(datastream, 14))
####
executionTime = (time.time() - startTime)
print("Execution time (ms): " + str(executionTime * 1000))