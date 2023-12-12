def day4():
    file = open("day4input.txt")
    content = file.read()
    parseinput_part2(content)
    #parseinput_part2("Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53\nCard 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19\nCard 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1\nCard 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83\nCard 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36\nCard 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11")
    file.close()

def parseinput_part1(text):
    sum = 0
    lines = text.splitlines()
    for l in lines:
        split = l.split(":")
        id = int(split[0].replace("Card ", ""))
        sections = split[1].split("|")
        winningNumbers = parseNumbers(sections[0])
        haveNumbers = parseNumbers(sections[1])
        count = getNumWinningNumbers(winningNumbers, haveNumbers)
        score = 0
        if count > 0:
            score = 1
            for i in range(0, count - 1):
                score *= 2
        sum += score

    print(sum)

def parseinput_part2(text):
    sum = 0
    scratchcardSet = {}
    lines = text.splitlines()
    for l in lines:
        split = l.split(":")
        id = int(split[0].replace("Card ", ""))
        scratchcardSet[id] = 1

    for l in lines:
        split = l.split(":")
        id = int(split[0].replace("Card ", ""))
        sections = split[1].split("|")
        winningNumbers = parseNumbers(sections[0])
        haveNumbers = parseNumbers(sections[1])
        count = getNumWinningNumbers(winningNumbers, haveNumbers)
        numScratchCards = scratchcardSet[id]
        for index in range(id + 1, id + count + 1):
            scratchcardSet[index] += numScratchCards

    for key, val in scratchcardSet.items():
        sum += val
    print(scratchcardSet)

    print(sum)

def parseNumbers(numbers):
    split = numbers.split()
    l = list()
    for item in split:
        l.append(int(item))
    return l

def getNumWinningNumbers(winningNumbers, haveNumbers):
    sum = 0
    for num in winningNumbers:
        if num in haveNumbers:
            sum += 1
    return sum
