
def day6():
    day6Input_part1 = [(48, 296), (93, 1928), (85, 1236), (95, 1391)]
    day6Input_part2 = [(48938595, 296192812361391)]
    day6_part1(day6Input_part2)

def day6_part1(input):
    output = 1
    for set in input:
        time = set[0]
        recordDistance = set[1]
        numPermutations = 0
        for i in range(1, time):
            distance = getDistanceFromTime(i, time - i)
            if (distance > recordDistance):
                numPermutations += 1
        print(numPermutations)
        output *= numPermutations
    print(output)

def getDistanceFromTime(chargeTime, runTime):
    return chargeTime * runTime
