import math

def day11():
    file = open("day11input.txt")
    content = file.read()
    parseInput(content)
    file.close()

def parseInput(text):
    galaxyLocs = list()
    rowssWithNoGalaxies = list()
    columnssWithNoGalaxies = list()
    lines = text.splitlines()
    for i in range(0, len(lines)):
        for j in range(0, len(lines[i])):
            if lines[i][j] == "#":
                galaxyLocs.append((i, j))

    for i in range(0, len(lines)):
        foundRow = False
        for pair in galaxyLocs:
            if pair[0] == i:
                foundRow = True
                break
        if foundRow == False:
            rowssWithNoGalaxies.append(i)

    for j in range(0, len(lines[0])):
        foundColumn = False
        for pair in galaxyLocs:
            if pair[1] == j:
                foundColumn = True
                break
        if foundColumn == False:
            columnssWithNoGalaxies.append(j)

    part1(galaxyLocs, len(lines), len(lines[0]), rowssWithNoGalaxies, columnssWithNoGalaxies)

def part1(galaxyLocs, lengthA, lengthB, rowssWithNoGalaxies, columnssWithNoGalaxies):
    sum = 0
    for i in range(0, len(galaxyLocs)):
        for j in range(i + 1, len(galaxyLocs)):
            pointA = galaxyLocs[i]
            pointB = galaxyLocs[j]
            distance = getDistance_taxicab(pointA, pointB, lengthA, lengthB, rowssWithNoGalaxies, columnssWithNoGalaxies, 1000000)
            print(str(pointA)+", "+str(pointB)+" = "+str(distance))
            sum += distance

    print("answer = "+str(sum))

def getDistance_taxicab(pointA, pointB, lenghA, lengthB, rowssWithNoGalaxies, columnssWithNoGalaxies, expansion):
    output = abs(pointB[1] - pointA[1]) + abs(pointB[0] - pointA[0])
    rowIntercept = 0
    columnIntercept = 0
    for i in rowssWithNoGalaxies:
        if (pointA[0] < i < pointB[0]) or (pointB[0] < i < pointA[0]):
            rowIntercept += 1
    for j in columnssWithNoGalaxies:
        if (pointA[1] < j < pointB[1]) or (pointB[1] < j < pointA[1]):
            columnIntercept += 1

    return output + (rowIntercept + columnIntercept) * (expansion - 1)

def getDistance_aStar(pointA, pointB, lenghA, lengthB, rowssWithNoGalaxies, columnssWithNoGalaxies):
    workingSet = []
    workingSet.append(pointA)
    cameFrom = {}
    gScore = {}
    fScore = {}
    gScore[pointA] = 0
    #fScore[pointA] = getPointCost(pointA, rowssWithNoGalaxies, columnssWithNoGalaxies)
    fScore[pointA] = 1

    while len(workingSet) > 0:
        currentBest = pointA
        lowestScore = math.inf
        for item in workingSet:
            if fScore.get(item, math.inf) < lowestScore:
                currentBest = item
                lowestScore = fScore.get(item, math.inf)
            if currentBest == pointB:
                return fScore[item] - 1


        workingPoint = workingSet.pop(0)
        neighbors = [(workingPoint[0] + 1, workingPoint[1]), (workingPoint[0] - 1, workingPoint[1]), (workingPoint[0], workingPoint[1] + 1), (workingPoint[0], workingPoint[1] - 1)]
        for point in neighbors:
            if point[0] < 0 or point[1] < 0 or point[0] > lenghA or point[1] > lengthB:
                continue
            tentative_gScore = gScore.get(workingPoint, math.inf) + getTravelCost(workingPoint, point, rowssWithNoGalaxies, columnssWithNoGalaxies)
            if tentative_gScore < gScore.get(point, math.inf):
                cameFrom[point] = workingPoint
                gScore[point] = tentative_gScore
                #fScore[point] = tentative_gScore + getPointCost(point, rowssWithNoGalaxies, columnssWithNoGalaxies)
                fScore[point] = tentative_gScore + 1
                if point not in workingSet:
                    workingSet.append(point)



    return 0

def getPointCost(point, rowssWithNoGalaxies, columnssWithNoGalaxies):
    #no expansion
    return 1

def getTravelCost(pointA, pointB, rowssWithNoGalaxies, columnssWithNoGalaxies):
    #no expansion
    #return 1
    #with expansion
    #pointAInZone = pointA[0] in rowssWithNoGalaxies or pointA[1] in columnssWithNoGalaxies
    pointBInZone = pointB[0] in rowssWithNoGalaxies or pointB[1] in columnssWithNoGalaxies
    if pointBInZone:
        return 2
    return 1
