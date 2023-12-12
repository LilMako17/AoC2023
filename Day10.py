import sys


def day10():
    file = open("day10input.txt")
    content = file.read()
    parseInput(content)
    file.close()

def parseInput(text):
    lines = text.splitlines()
    startPos = (-1, -1)
    for i in range(0, len(lines)):
        for j in range(0, len(lines[i])):
            if lines[i][j] == "S":
                startPos = (i, j)

    print("start: "+str(startPos))
    dirs = findConnectedDirs(lines, startPos[0], startPos[1])
    queue = []
    visited = list()
    visited.append(startPos)
    for dir in dirs:
        currentPos = (startPos[0]+dir[0], startPos[1]+dir[1])
        queue.append((currentPos, dir, 1))

    while len(queue) > 0:
        workingObj = queue.pop(0)
        currentPos = workingObj[0]
        prevDir = workingObj[1]
        distance = workingObj[2]
        if currentPos in visited:
            print("answer: "+str(distance)+" ---> current pos "+str(currentPos)+" "+getValue(lines, currentPos[0], currentPos[1]))
            break
        visited.append(currentPos)
        value = getValue(lines, currentPos[0], currentPos[1])
        dir = getNextDirection(prevDir, value)
        nextPos = (currentPos[0] + dir[0], currentPos[1] + dir[1])
        queue.append((nextPos, dir, distance + 1))

def getNextDirection(previousDir, currentSymbol):
    if currentSymbol == "|":
        if previousDir == (1, 0):
            return (1, 0)
        elif previousDir == (-1, 0):
            return (-1, 0)
        else:
            print("error: "+currentSymbol+" dir: "+str(previousDir))
    if currentSymbol == "-":
        if previousDir == (0, 1):
            return (0, 1)
        elif previousDir == (0, -1):
            return (0, -1)
        else:
            print("error: "+currentSymbol+" dir: "+str(previousDir))
    if currentSymbol == "L":
        if previousDir == (0, -1):
            return (-1, 0)
        elif previousDir == (1, 0):
            return (0, 1)
        else:
            print("error: "+currentSymbol+" dir: "+str(previousDir))
    if currentSymbol == "J":
        if previousDir == (0, 1):
            return (-1, 0)
        elif previousDir == (1, 0):
            return (0, -1)
        else:
            print("error: "+currentSymbol+" dir: "+str(previousDir))
    if currentSymbol == "7":
        if previousDir == (0, 1):
            return (1, 0)
        elif previousDir == (-1, 0):
            return (0, -1)
        else:
            print("error: "+currentSymbol+" dir: "+str(previousDir))
    if currentSymbol == "F":
        if previousDir == (0, -1):
            return (1, 0)
        elif previousDir == (-1, 0):
            return (0, 1)
        else:
            print("error: "+currentSymbol+" dir: "+str(previousDir))
    return previousDir

def findConnectedDirs(lines, i, j):
    output = list()
    left = getValue(lines, i, j - 1)
    right = getValue(lines, i, j + 1)
    up = getValue(lines, i - 1, j)
    down = getValue(lines, i + 1, j)
    if left == "-" or left == "L" or left == "F":
        output.append((0, -1))
    if right == "-" or right == "7" or right == "J":
        output.append((0, 1))
    if up == "|" or up == "7" or up == "F":
        output.append((-1, 0))
    if down == "|" or down == "J" or down == "L":
        output.append((1, 0))
    return output

def getValue(lines, i, j):
    if 0 <= i < len(lines) and 0 <= j < len(lines[i]):
        return lines[i][j]
    return "."
