from aocd import get_data
data: int = []

for line in get_data(day=2, year=2015).splitlines(False):
    data.append([int(x) for x in line.split('x')])

# part 1
paper = 0
for i in data:
    dimension = [i[0] * i[1], i[1] * i[2], i[0] * i[2]]
    paper += dimension[0] * 2 + dimension[1] * 2 + dimension[2] * 2 + min(dimension)
print(paper)

# part 2
ribbon = 0
for i in data:
    s = sorted(i)
    ribbon += s[0] * 2 + s[1] * 2 + i[0] * i[1] * i[2]
print(ribbon)