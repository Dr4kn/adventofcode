from aocd import get_data
houses = {}
row = 0
column = 0
houses[row, column] = 1

#part 1
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

santa_row = 0
santa_column = 0
robo_row = 0
robo_column = 0
houses = {}
houses[0, 0] = 1
santa = True

#part 2
for move in get_data(day=3, year=2015):
    if santa:
        row = santa_row
        column = santa_column
    else:
        row = robo_row
        column = robo_column
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
    if santa:
        santa_row = row
        santa_column = column
    else:
        robo_row = row
        robo_column = column
    santa = False if santa else True

print(len(houses.values()))