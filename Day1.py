def day1sol1(string_in):
    sum = 0
    split = string_in.splitlines()
    for line in split:

        first_number = 0
        second_number = 0

        for char in line:
            if char.isdecimal():
                first_number = int(char) * 10
                break
        for char in reversed(line):
            if char.isdecimal():
                second_number = int(char)
                break

        sum += first_number + second_number
    print(sum)

def day1sol2(string_in):
    sum = 0
    split = string_in.splitlines()
    for line in split:

        first_number = 0
        second_number = 0

        first_index = len(line) + 1
        last_index = -1

        for i, v in enumerate(line):
            num = getnumber(line, i)
            if num >= 0:
                if i < first_index:
                    first_number = num * 10
                    first_index = i
                if i > last_index:
                    second_number = num
                    last_index = i

        #print(line+" "+str(first_number+second_number))

        sum += first_number + second_number
    print(sum)

def getnumber(line, index) -> int:
    for i, v in enumerate(line):
        if i >= index:
            if v.isdecimal():
                return int(v)
            if line[index:].startswith("one"):
                return 1
            if line[index:].startswith("two"):
                return 2
            if line[index:].startswith("three"):
                return 3
            if line[index:].startswith("four"):
                return 4
            if line[index:].startswith("five"):
                return 5
            if line[index:].startswith("six"):
                return 6
            if line[index:].startswith("seven"):
                return 7
            if line[index:].startswith("eight"):
                return 8
            if line[index:].startswith("nine"):
                return 9
            #if line[index:].startswith("zero"):
            #    return 0
            return -1



def day1():
    file = open("day1input.txt")
    content = file.read()
    day1sol2(content)
    file.close()