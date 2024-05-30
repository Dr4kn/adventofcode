from aocd import get_data

floor = 0
count = 0
basement = False
for i in get_data(day=1, year=2015):
    floor = floor + 1 if i == '(' else floor - 1
    count += 1
    if floor == -1 and basement == False:
        basement = True
        print(count)
print(floor)

