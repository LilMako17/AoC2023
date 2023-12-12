import numpy as np

def parsegame(line):
    sets = line.split(";")
    output = list()
    for s in sets:
        rgb = [0, 0, 0]
        items = s.split(",")
        for it in items:
            pair = it.split()
            count = int(pair[0])
            if pair[1] == "red":
                rgb[0] = count
            if pair[1] == "green":
                rgb[1] = count
            if pair[1] == "blue":
                rgb[2] = count
        output.append(rgb)
    return output

def parseinput_part1(text):
    sum = 0
    lines = text.splitlines()
    for l in lines:
        split = l.split(":")
        id = int(split[0].replace("Game ", ""))
        gameresult = parsegame(split[1])
        #print(l+" ->>>> "+str(id)+" "+str(gameresult))
        if isvalid((gameresult)):
            sum += id

    print(sum)

def isvalid(gameresult):
    for set in gameresult:
        if set[0] > 12 or set[1] > 13 or set[2] > 14:
            return False
    return True

def parseinput_part2(text):
    sum = 0
    lines = text.splitlines()
    for l in lines:
        split = l.split(":")
        id = int(split[0].replace("Game ", ""))
        gameresult = parsegame(split[1])
        minset = getminset(gameresult)
        power = minset[0] * minset[1] * minset[2]
        sum += power

    print(sum)

def getminset(gameresult):
    min = [0, 0, 0]
    for set in gameresult:
        if set[0] > min[0]:
            min[0] = set[0]
        if set[1] > min[1]:
            min[1] = set[1]
        if set[2] > min[2]:
            min[2] = set[2]
    return min

def day2():
    file = open("day2input.txt")
    content = file.read()
    parseinput_part2(content)
    file.close()