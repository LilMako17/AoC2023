from itertools import groupby

def day12():
    file = open("day12input.txt")
    content = file.read()
    #parseInput_part2("???.### 1,1,3")
    #parseInput_part2(".??..??...?##. 1,1,3")
    #parseInput_part2("?#?#?#?#?#?#?#? 1,3,1,6")
    #parseInput_part2("????.#...#... 4,1,1")
    #parseInput_part2("????.######..#####. 1,6,5")
    #parseInput_part2("?###???????? 3,2,1")
    parseInput_part2(content)
    file.close()

def parseInput_part1(text):
    lines = text.splitlines()
    sum = 0
    for line in lines:
        split = line.split()
        picross = split[0]
        numbers = list(map(int, split[1].split(",")))
        num = getNumPossibilities(picross, numbers)
        print(str(num)+" <----- "+line)
        sum += num

    print("answer = "+str(sum))

def parseInput_part2(text):
    lines = text.splitlines()
    sum = 0
    for line in lines:
        split = line.split()
        picross = split[0]
        numbers = list(map(int, split[1].split(",")))
        expandedPicross = ""
        expandedNumbers = []
        for i in range(0, 5):
            if (i >= 1):
                expandedPicross += "?"
            expandedPicross += picross
            for item in numbers:
                expandedNumbers.append(item)
        num = getNumPossibilities(expandedPicross, expandedNumbers)
        print(str(num) + " <----- " + expandedPicross+" "+str(expandedNumbers))
        sum += num

    print("answer = " + str(sum))

def getNumPossibilities(picross, numbers):
    #print("working text len: "+str(len(picross)))
    validAnswer = 0
    workQueue = []
    workQueue.append((picross, numbers, 0))
    while len(workQueue) > 0:
        workingItem = workQueue.pop()
        workingText = workingItem[0]
        workingNumbers = workingItem[1]
        workingIndex = workingItem[2]
        if len(workingNumbers) == 0:
            anyLeft = False
            for lookAhead in range(workingIndex + 1, len(workingText)):
                if workingText[lookAhead] == "#":
                    anyLeft = True
                    break
            if not anyLeft:
                #print("IS VALID : "+workingText)
                validAnswer += 1
        elif workingIndex >= len(workingText):
            #print("NO VALID: "+workingText)
            #not valid answer
            continue
        else:
            newWorkItems = checkString(workingText, workingIndex, workingNumbers)
            #print("returned "+str(len(newWorkItems))+" from checking "+str(workingItem))
            for item in newWorkItems:
                workQueue.append(item)
    return validAnswer

def checkString(picross, workingIndex, numbers):
    workingChar = picross[workingIndex]
    if workingChar == ".":
        return [(picross, numbers, workingIndex + 1)]
    elif workingChar == "#":
        lookAhead = workingIndex
        count = 0
        desiredVal = numbers[0]
        while lookAhead < len(picross) and picross[lookAhead] != ".":
            lookAhead += 1
            count += 1
            if count == desiredVal:
                if lookAhead >= len(picross) or picross[lookAhead] == ".":
                    del numbers[0]
                    workingIndex += desiredVal
                    return [(picross, list(numbers), workingIndex)]
                elif picross[lookAhead] == "#":
                    return []
                elif picross[lookAhead] == "?":
                    del numbers[0]
                    workingIndex += desiredVal
                    newStringA = picross[:workingIndex] + "." + picross[workingIndex + 1:]
                    return [(newStringA, list(numbers), workingIndex)]
        return []
    elif workingChar == "?":
        newStringA = picross[:workingIndex] + "." + picross[workingIndex + 1:]
        newStringB = picross[:workingIndex] + "#" + picross[workingIndex + 1:]
        return [(newStringA, list(numbers), workingIndex), (newStringB, list(numbers), workingIndex)]

    print("ERROR unknown char "+workingChar)
    return []

def substrings(s):
    output = list()
    for char, group in groupby(s):
        substr = ''
        for i in group:
            substr += i
        output.append(substr)
    return output
