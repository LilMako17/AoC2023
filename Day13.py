import copy

def day13():
    file = open("day13input.txt")
    content = file.read()
    parseInput(content)
    file.close()

def parseInput(text):
    sets = list()
    workingSet = list()
    for line in text.splitlines():
        if line == "":
            sets.append(workingSet)
            workingSet = list()
        else:
            workingSet.append(line)
    sets.append(workingSet)

    #part1(sets)
    part2(sets)

def part1(sets):
    sum = 0
    count = 1
    for set in sets:
        vertReflection = findVerticalReflection(set)
        #print(str(count)+" v reflection: "+str(vertReflection))

        # transform rows to columns
        horzTranform = list(zip(*reversed(set)))
        horzReflection = findVerticalReflection(horzTranform)
        #print(str(count)+" h reflection: "+str(horzReflection))
        count += 1
        sum += vertReflection * 100
        sum += horzReflection

    print(sum)

def part2(sets):
    sum = 0
    count = 1
    for set in sets:

        vertReflection = findVerticalReflection(set)
        #print(str(count) + " OLD v reflection: " + str(vertReflection))
        #if (vertReflection != 0):
        for i in range(0, len(set)):
            for j in range(0, len(set[i])):
                permutation = copy.deepcopy(set)
                if permutation[i][j] == ".":
                    permutation[i] = permutation[i][:j] + "#" + permutation[i][j + 1:]
                if permutation[i][j] == "#":
                    permutation[i] = permutation[i][:j] + "." + permutation[i][j + 1:]
                newVReflect = findVerticalReflection(permutation)
                if newVReflect != 0 and newVReflect != vertReflection:
                    print(str(count)+" NEW v reflection: "+str(newVReflect))
                    vertReflection = newVReflect
                    set = permutation
                    break

        # transform rows to columns
        horzReflection = 0
        if (vertReflection == 0):
            horzTranform = list(zip(*reversed(set)))
            horzReflection = findVerticalReflection(horzTranform)
            #print(str(count)+" OLD h reflection: "+str(horzReflection))
            for i in range(0, len(horzTranform)):
                for j in range(0, len(horzTranform[i])):
                    permutation = copy.deepcopy(horzTranform)
                    strLine = str(permutation[i])
                    if permutation[i][j] == ".":
                        permutation[i] = strLine[:j] + "#" + strLine[j + 1:]
                    if permutation[i][j] == "#":
                        permutation[i] = strLine[:j] + "." + strLine[j + 1:]
                    newHReflect = findVerticalReflection(permutation)
                    if newHReflect != 0 and newHReflect != horzReflection:
                        print(str(count)+" NEW h reflection: "+str(newHReflect))
                        horzReflection = newHReflect
                        break

        count += 1
        sum += vertReflection * 100
        sum += horzReflection

    print(sum)


def findVerticalReflection(set):
    #middleIndex = math.floor(len(set) / 2)
    #start at middle and work outwards in both directions
    for i in range(0, len(set)):
        workingIndexA = i
        if isMirrored(set, workingIndexA):
            return workingIndexA
    return 0

def isMirrored(set, index):
    if index <= 0 or index >= len(set):
        return False

    numLinesMirrored = 0
    isMirrored = True
    for i in range(0, index * 2):
        indexA = index + i
        indexB = index - i - 1
        if (indexA >= len(set) or indexB < 0):
            return numLinesMirrored > 0
        lineA = set[indexA]
        lineB = set[indexB]
        if lineA == lineB:
            numLinesMirrored += 1
        else:
            isMirrored = False
            break
    return isMirrored