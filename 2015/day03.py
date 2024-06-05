from aocd import get_data
houses = {}
row = 0
column = 0
houses[row, column] = 1

for move in get_data(day=3, year=2015):
    if move == '>':
        row = row + 1
    elif move == '<':
        row = row - 1
    elif move == '^':
        column = column + 1
    elif move == 'v':
        column = column - 1
    if (row, column) in houses:
        x = houses.get((row, column))
        houses.update({(row, column) : x + 1})
    else:
        houses[row, column] = 1

print(len(houses.values()))