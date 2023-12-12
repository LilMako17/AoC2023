import math


def day8():
    file = open("day8input.txt")
    content = file.read()
    partInput(content)
    file.close()

def partInput(text):
    lineIndex = 0
    directions = ""
    mapLeft = {}
    mapRight = {}
    for line in text.splitlines():
        if lineIndex == 0:
            directions = line
        elif len(line) == 16:
            startPos = line[0:3]
            rightDir = line[12:15]
            leftDir = line[7:10]
            mapLeft[startPos] = leftDir
            mapRight[startPos] = rightDir
            #print(startPos+" : "+rightDir+" : "+leftDir)
        lineIndex += 1

    part2(directions, mapLeft, mapRight)

def part1(directions, mapLeft, mapRight):
    currentPos = "AAA"
    stepCount = 0
    while currentPos != "ZZZ" and stepCount < (10**10):
        if currentPos in mapLeft.keys() and currentPos in mapRight.keys():
            dir = directions[stepCount % len(directions)]
            if dir == "L":
                currentPos = mapLeft[currentPos]
            elif dir == "R":
                currentPos = mapRight[currentPos]
            else:
                print("ERROR direction not recognized: "+dir)
            stepCount += 1
        else:
            print("ERROR key not found: "+currentPos)
            break
    print(stepCount)

def part2(directions, mapLeft, mapRight):
    stepCount = list()
    currentPosList = list()
    for key in mapLeft.keys():
        if key[2] == "A":
            currentPosList.append(key)
            stepCount.append(0)
    print("checking "+str(currentPosList))
    while not allReachedDestination(currentPosList):
        for i in range(0, len(currentPosList)):
            currentPos = currentPosList[i]
            if currentPos[2] != "Z":
                if currentPos in mapLeft.keys() and currentPos in mapRight.keys():
                    dir = directions[stepCount[i] % len(directions)]
                    if dir == "L":
                        currentPosList[i] = mapLeft[currentPos]
                    elif dir == "R":
                        currentPosList[i] = mapRight[currentPos]
                    else:
                        print("ERROR direction not recognized: "+dir)
                    stepCount[i] += 1
                else:
                    print("ERROR key not found: "+currentPos)
                    break
    print(str(stepCount))
    answer = lcm(*stepCount)
    print(answer)

def lcm(*integers):
    a = integers[0]
    for b in integers[1:]:
        a = (a * b) // math.gcd(a, b)
    return a

def allReachedDestination(currentPosList):
    for entry in currentPosList:
        if entry[2] != "Z":
            return False
    return True
