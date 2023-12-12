from functools import cmp_to_key

def day7():
    file = open("day7input.txt")
    content = file.read()
    parseinput_part1(content)
    file.close()

def parseinput_part1(text):
    hands = list()
    for line in text.splitlines():
        set = line.split()
        hand = set[0]
        bet = int(set[1])
        tup = (hand, bet)
        hands.append(tup)

    hands = sorted(hands, key=cmp_to_key(sorthands), reverse=True)

    sum = 0
    index = 0
    for h in hands:
        index += 1
        print(str(index)+" "+h[0]+" "+str(h[1]))
        bet = h[1]
        sum += index * bet

    print(sum)

def sorthands(a, b):
    handA = a[0]
    handB = b[0]
    rankA = getHandRank(handA)
    rankB = getHandRank(handB)
    if rankA == rankB:
        for i in range(0, len(handA)):
            if handA[i] != handB[i]:
                return compareCard(handA[i], handB[i])
    return rankA - rankB

def compareCard(a, b):
    rank_part1 = "A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2"
    rank_part2 = "A, K, Q, T, 9, 8, 7, 6, 5, 4, 3, 2, J"
    return rank_part2.index(a) - rank_part2.index(b)

def getHandRank(hand):
    buckets = {}
    for card in hand:
        if card in buckets.keys():
            buckets[card] += 1
        else:
            buckets[card] = 1

    if isFiveOfAKind(buckets):
        return 1
    elif isFourOfAKind(buckets):
        return 2
    elif isFullHouse(buckets):
        return 3
    elif isThreeOfAKind(buckets):
        return 4
    elif isTwoPair(buckets):
        return 5
    elif isOnePair(buckets):
        return 6
    return 7

joker = 'J'
def isFiveOfAKind(hand):
    if len(hand.keys()) == 1:
        return True
    if len(hand.keys()) == 2 and joker in hand.keys():
        return True
    return False
def isFourOfAKind(hand):
    keys = list(hand.keys())
    maxSet = 0
    numJokers = hand.get(joker, 0)
    for k in keys:
        if k != joker and hand[k] > maxSet:
            maxSet = hand[k]
    return maxSet + numJokers >= 4
def isFullHouse(hand):
    keys = list(hand.keys())
    maxSet1 = 0
    maxSet2 = 0
    numJokers = hand.get(joker, 0)
    for k in keys:
        if k != joker and hand[k] > maxSet1:
            maxSet2 = maxSet1
            maxSet1 = hand[k]
        elif k != joker and hand[k] > maxSet2:
            maxSet2 = hand[k]
    return maxSet1 + maxSet2 + numJokers >= 5
def isThreeOfAKind(hand):
    keys = list(hand.keys())
    maxSet = 0
    numJokers = hand.get(joker, 0)
    for k in keys:
        if k != joker and hand[k] > maxSet:
            maxSet = hand[k]
    return maxSet + numJokers >= 3
def isTwoPair(hand):
    keys = list(hand.keys())
    maxSet1 = 0
    maxSet2 = 0
    numJokers = hand.get(joker, 0)
    for k in keys:
        if k != joker and hand[k] > maxSet1:
            maxSet2 = maxSet1
            maxSet1 = hand[k]
        elif k != joker and hand[k] > maxSet2:
            maxSet2 = hand[k]
    return maxSet1 + maxSet2 + numJokers >= 4
def isOnePair(hand):
    keys = list(hand.keys())
    maxSet = 0
    numJokers = hand.get(joker, 0)
    for k in keys:
        if k != joker and hand[k] > maxSet:
            maxSet = hand[k]
    return maxSet + numJokers >= 2
