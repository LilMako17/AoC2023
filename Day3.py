def day3():
    file = open("day3input.txt")
    content = file.read()
    day3sol2(content)
    file.close()


def parseInput(text):
    output = list()
    for line in text.splitlines():
        output.append(line)
    return output

def day3sol1(text):
    sum = 0
    grid = parseInput(text)
    i = 0
    while i < len(grid):
        j = 0
        while j < len(grid[i]):
            char = grid[i][j]
            if char.isdecimal():
                number = getNumber(grid, i, j)
                if number > 0:
                    length = len(str(number))
                    for counter in range(j, j + length):
                        if isAdjacentToSymbol(grid, i, counter):
                            sum += number
                            break
                    j += length - 1
            j += 1
        i += 1
    print(sum)

def day3sol2(text):
    sum = 0
    gearMap = {}
    grid = parseInput(text)
    i = 0
    while i < len(grid):
        j = 0
        while j < len(grid[i]):
            char = grid[i][j]
            if char.isdecimal():
                number = getNumber(grid, i, j)
                if number > 0:
                    length = len(str(number))
                    for counter in range(j, j + length):
                        key = isAdjacentToGear(grid, i, counter)
                        if key != (-1, -1):
                            if key in gearMap.keys():
                                gearMap[key].append(number)
                            else:
                                gearMap[key] = list()
                                gearMap[key].append(number)
                            break
                    j += length - 1
            j += 1
        i += 1

    for key, value in gearMap.items():
        if len(value) == 2:
            sum += value[0] * value[1]
    print(sum)

def getNumber(grid, x, y):
    line = grid[x]
    count = 0
    while y + count < len(line) and line[y + count].isdecimal():
        count += 1
    return int(line[y:y+count])

def isAdjacentToSymbol(grid, x, y):
    for i in range(- 1, 2):
        for j in range(- 1, 2):
            char = searchGrid(grid, i + x, j + y)
            if char != "." and not char.isdecimal():
                return True
    return False

def isAdjacentToGear(grid, x, y):
    for i in range(- 1, 2):
        for j in range(- 1, 2):
            char = searchGrid(grid, i + x, j + y)
            if char == "*":
                return i + x, j + y
    return -1, -1

def searchGrid(grid, x, y):
    if 0 <= x < len(grid) and 0 <= y < len(grid[x]):
        return grid[x][y]
    return "."
