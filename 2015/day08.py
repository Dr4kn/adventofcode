from aocd import get_data
import re

def part1():
    string_length = 0
    memory_length = 0

    for line in data.splitlines(False):
        string_length += len(line)
        memory_length += len(re.sub(r"\\\"|\\x..|\\\\", "a", line[1:-1]))
    
    print("part1: " + str(string_length - memory_length))

def part2():
    string_length = 0
    encoded_length = 0

    for line in data.splitlines(False):
        string_length += len(line)
        encoded_length += len(re.sub(r"\"|\\", "aa", line)) + 2
    print("part2: " + str(encoded_length - string_length))

if __name__ == "__main__":
    data = get_data(day=8, year=2015)
    part1()
    part2()