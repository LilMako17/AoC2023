
def day5():
    file = open("day5input.txt")
    content = file.read()
    parseinput(content)
    file.close()

def parseinput(text):
    seeds = list()
    seedToSoilMap = MapObject("seed", "soil")
    soilToFertilizerMap = MapObject("soil", "fertilizer")
    fertilizerToWaterMap = MapObject("fertilizer", "water")
    waterToLightMap = MapObject("water", "light")
    lightToTempMap = MapObject("light", "temperature")
    tempToHumidityMap = MapObject("temperature", "humidity")
    humidityToLocMap = MapObject("humidity", "location")

    workingObj = {}
    for line in text.splitlines():
        if "seeds:" in line:
            spl = line.split(":")[1].split()
            count = len(spl)
            for index in range(0, count):
                #art 1
                seeds.append(int(spl[index]))

        elif "seed-to-soil map:" in line:
            workingObj = seedToSoilMap
        elif "soil-to-fertilizer map:" in line:
            workingObj = soilToFertilizerMap
        elif "fertilizer-to-water map:" in line:
            workingObj = fertilizerToWaterMap
        elif "water-to-light map:" in line:
            workingObj = waterToLightMap
        elif "light-to-temperature map:" in line:
            workingObj = lightToTempMap
        elif "temperature-to-humidity map:" in line:
            workingObj = tempToHumidityMap
        elif "humidity-to-location map:" in line:
            workingObj = humidityToLocMap
        elif len(line) > 0:
            split = line.split()
            sourceStart = int(split[0])
            destStart = int(split[1])
            r = int(split[2])
            workingObj.addMap(sourceStart, destStart, r)

    lowest = 0
    for seed in seeds:
        val = seedToSoilMap.findDest(seed)
        val = soilToFertilizerMap.findDest(val)
        val = fertilizerToWaterMap.findDest(val)
        val = waterToLightMap.findDest(val)
        val = lightToTempMap.findDest(val)
        val = tempToHumidityMap.findDest(val)
        val = humidityToLocMap.findDest(val)
        #print(str(seed)+" -> "+str(val))
        if (lowest == 0 or val < lowest):
            lowest = val
    print("part 1 answer "+str(lowest))

def isValidLocation(seed, seedList):
    count = len(seedList)
    for index in range(0, count):
        if (index %2 == 0):
            sourceStart = seedList[index]
            r = seedList[index + 1]
            if seed >= sourceStart and seed < sourceStart + r:
                return True
    return False

class MapObject:
    def __init__(self, source, dest):
        self.sourceName = source
        self.destName = dest
        self.maps = list()

    def addMap(self, sourceStart, destStart, range):
        blob = [destStart, sourceStart, range]
        self.maps.append(blob)

    def findDest(self, source):
        for set in self.maps:
            sourceStart = set[0]
            destStart = set[1]
            range = set[2]
            if source >= sourceStart and source < sourceStart + range:
                return destStart + (source - sourceStart)
        return source

    def findSource(self, dest):
        for set in self.maps:
            sourceStart = set[0]
            destStart = set[1]
            range = set[2]
            if dest >= destStart and dest < destStart + range:
                return sourceStart + (dest - destStart)
        return dest