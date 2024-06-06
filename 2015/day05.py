from aocd import get_data
data = get_data(day=5, year=2015)

def part1():
    nice_string = 0
    for line in data.splitlines(False):
        double_letter = False
        vowels = 0
        if line[-1] in "aeiou":
            vowels += 1
        for i in range(len(line) - 1):
            substring = line[i:i+2]
            if substring == "ab" or substring == "cd" or substring == "pq" or substring == "xy":
                break
            if substring[0] == substring[1]:
                double_letter = True
            if line[i] in "aeiou":
                vowels += 1
            if i == 14 and double_letter and vowels >= 3:
                nice_string += 1

    print("part1: " + str(nice_string))

def part2():
    nice_string = 0
    for line in data.splitlines(False):
        space_repeat = False
        letter_pair = False
        for i in range(len(line) - 2):
            if line[i] + line[i+1] in line[i+2:]:
                letter_pair = True
            if line[i] == line[i + 2]:
                space_repeat = True
            if letter_pair and space_repeat:
                nice_string += 1
                break

    print("part2: " + str(nice_string))

if __name__ == "__main__":
    part1()
    part2()
