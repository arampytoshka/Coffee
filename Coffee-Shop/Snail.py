up = 5
down = 2
height = 10
way = 0
day = 0
for day in range(100):
    if way < height:
        way = way + up
        if way < height:
            way = way - down
    day = day + 1
    if way >= height:
        break
print(day)
print(way)