import time
import hashlib

def day14():
    file = open("day14input.txt")
    content = file.read()
    parseInput(content)
    file.close()

def parseInput(text):
    grid = list()
    for line in text.splitlines():
        arr = list()
        for char in line:
            arr.append(char)
        grid.append(arr)

    Part2(grid)

def Part1(grid):
    grid = TranslateNorth(grid)
    sum = 0
    for i in range(0, len(grid)):
        line = grid[i]
        value = len(grid) - i
        for c in line:
            if c == "O":
                sum += value

    print(sum)

def getCacheResult(cachedResults, input, func):
    strInput = toKey(input)
    if strInput in cachedResults:
        #print("cache hit")
        return cachedResults[strInput]

    output = func(input)
    cachedResults[toKey(output)] = strInput

    return output

def toKey(grid):
    hashId = hashlib.md5()
    hashId.update(repr(grid).encode('utf-8'))
    return hashId.hexdigest()

def Part2(grid):
    startTime = time.process_time()
    cachedResults = {}
    for i in range(0, 1000000000):
        grid = getCacheResult(cachedResults, grid, TranslateNorth)
        grid = getCacheResult(cachedResults, grid, TranslateWest)
        grid = getCacheResult(cachedResults, grid, TranslateSouth)
        grid = getCacheResult(cachedResults, grid, TranslateEast)
        if i % 10000 == 0:
            print(str(i)+" time = "+str(time.process_time() - startTime))
            startTime = time.process_time()
            print(len(cachedResults))
    sum = 0
    for i in range(0, len(grid)):
        line = grid[i]
        value = len(grid) - i
        for c in line:
            if c == "O":
                sum += value
        #print(line)

    print(sum)

def TranslateNorth(grid):
    for i in range(0, len(grid)):
        workingIndex = i
        targetIndex = workingIndex - 1
        while targetIndex >= 0:
            for j in range(0, len(grid[i])):
                if grid[workingIndex][j] == "O" and grid[targetIndex][j] == ".":
                    grid[targetIndex][j] = "O"
                    grid[workingIndex][j] = "."
            workingIndex = workingIndex - 1
            targetIndex = targetIndex - 1

    return grid

def TranslateWest(grid):
    for j in range(0, len(grid[0])):
        workingIndex = j
        targetIndex = workingIndex - 1
        while targetIndex >= 0:
            for i in range(0, len(grid)):
                if grid[i][workingIndex] == "O" and grid[i][targetIndex] == ".":
                    grid[i][targetIndex] = "O"
                    grid[i][workingIndex] = "."
            workingIndex = workingIndex - 1
            targetIndex = targetIndex - 1

    return grid

def TranslateEast(grid):
    for j in range(0, len(grid[0])):
        workingIndex = len(grid[0]) - j - 1
        targetIndex = workingIndex + 1
        while targetIndex < len(grid[0]):
            for i in range(0, len(grid)):
                if grid[i][workingIndex] == "O" and grid[i][targetIndex] == ".":
                    grid[i][targetIndex] = "O"
                    grid[i][workingIndex] = "."
            workingIndex = workingIndex + 1
            targetIndex = targetIndex + 1

    return grid

def TranslateSouth(grid):
    for i in range(0, len(grid)):
        workingIndex = len(grid) - i - 1
        targetIndex = workingIndex + 1
        while targetIndex < len(grid):
            for j in range(0, len(grid[i])):
                if grid[workingIndex][j] == "O" and grid[targetIndex][j] == ".":
                    grid[targetIndex][j] = "O"
                    grid[workingIndex][j] = "."
            workingIndex = workingIndex + 1
            targetIndex = targetIndex + 1

    return grid