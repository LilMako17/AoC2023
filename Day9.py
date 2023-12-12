def day9():
    file = open("day9input.txt")
    content = file.read()
    part1(content)
    file.close()

def part1(text):
    sum = 0
    for line in text.splitlines():
        sequence = list()
        for entry in line.split():
            sequence.append(int(entry))
        value = getPredictedValue(sequence)
        sum += value
    print("answer: "+str(sum))

def getPredictedValue(sequence):
    print("")
    count = 0
    print(sequence)
    diffs = list()
    diffs.append(sequence)
    while True:
        diff = getDiffSequence(sequence)
        count += 1
        print(str(diff))
        diffs.append(diff)
        if isAllZero(diff):
            break
        else:
            sequence = diff

    #part 1
    #sum = 0
    #for l in diffs:
    #    sum += l[len(l) - 1]
    #return sum

    #part 2
    prevVal = 0
    for i in range(1, len(diffs) + 1):
        index = len(diffs) - i
        val = diffs[index][0]
        prevVal = val - prevVal
    print("sum = "+str(prevVal))
    return prevVal



def getDiffSequence(sequence):
    output = list()
    for i in range(0, len(sequence) - 1):
        diff = sequence[i + 1] - sequence[i]
        output.append(diff)
    return output

def isAllZero(sequence):
    for entry in sequence:
        if entry != 0:
            return False
    return True
