from aocd import get_data
import re
data = get_data(day=6, year=2015)
parsed = [re.split(" through |,| ", line)for line in data.splitlines(False)]

def part1():
    rows, cols = (1000, 1000)
    arr = [[0 for i in range(cols)] for j in range(rows)]
    for line in parsed:
        frow, trow = (int(line[-4]), int(line[-2]))
        fcol, tcol = (int(line[-3]), int(line[-1]))

        counter = 0
        for row in range(frow, trow + 1):
            for col in range(fcol, tcol + 1):
                counter += 1
                if line[0] == "turn":
                    arr[row][col] = 1 if line[1] == "on" else 0
                else:
                    arr[row][col] = 1 if arr[row][col] == 0 else 0

    lights_on = 0
    for row in range(0,1000):
        for col in range(0,1000):
            if arr[row][col] == 1:
                lights_on += 1
    print("part1: " + str(lights_on))

def part2():
    rows, cols = (1000, 1000)
    arr = [[0 for i in range(cols)] for j in range(rows)]
    for line in parsed:
        frow, trow = (int(line[-4]), int(line[-2]))
        fcol, tcol = (int(line[-3]), int(line[-1]))

        counter = 0
        for row in range(frow, trow + 1):
            for col in range(fcol, tcol + 1):
                counter += 1
                if line[0] == "turn":
                    if line[1] == "off":
                        if arr[row][col] > 0:
                            arr[row][col] -= 1
                    else:
                        arr[row][col] += 1
                else:
                    arr[row][col] += 2 

    brightness = 0
    for row in range(0,1000):
        for col in range(0,1000):
                brightness += arr[row][col]
    print("part1: " + str(brightness))

if __name__ == "__main__":
    part1()
    part2()