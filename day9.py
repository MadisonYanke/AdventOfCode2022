import time
startTime = time.time()
#####
lines = open("./day9", "r").read().splitlines()\

def moveTail(head, tail):
    if abs(head[0] - tail[0]) < 2 and abs(head[1] - tail[1]) < 2:
        return
    elif abs(head[0] - tail[0]) == 2 and abs(head[1] - tail[1]) == 2:
        tail[0] = int(head[0] + (tail[0] - head[0])/2)
        tail[1] = int(head[1] + (tail[1] - head[1])/2)
    elif abs(head[0] - tail[0]) == 2:
        tail[0] = int(head[0] + (tail[0] - head[0])/2)
        tail[1] =  head[1]
    elif abs(tail[1] - head[1]) == 2:
        tail[0] = head[0]
        tail[1] = int(head[1] + (tail[1] - head[1])/2)

def moveRope(input, size):
    tailVisited = set()

    knots = []
    for i in range(size):
        knots.append([0,0])
    
    for line in input:
        direction, distance = line.split(' ')[0], int(line.split(' ')[1])
        for dist in range(1, distance+1):
            for i, knot in enumerate(knots):
                if i == 0:
                    match direction:
                        case "R":
                            knots[i] = [knot[0] + 1, knot[1]]
                        case "L":
                            knots[i] = [knot[0] - 1, knot[1]]
                        case "D":
                            knots[i] = [knot[0], knot[1] - 1]
                        case "U":
                            knots[i] = [knot[0], knot[1] + 1]
                else: 
                    moveTail(knots[i-1], knots[i])
                tailVisited.add(str(knots[-1]).zfill(3) + str(knots[-1]).zfill(3))
        
    return tailVisited


print("pt1: ", len(moveRope(lines, 2)), " pt2: ", len(moveRope(lines, 10)))
####
executionTime = (time.time() - startTime)
print("Execution time (ms): " + str(executionTime * 1000))