def xy(coord):
    x = 0
    y = 0
    for xy in coord:
        if xy == '^':
            x += 1
        elif xy == 'v':
            x -= 1
        elif xy == '>':
            y += 1
        elif xy == '<':
            y -= 1
        coords.add((x,y))

coord_input = list(raw_input())
santa = coord_input[0::2]
robot = coord_input[1::2]
coords = {(0,0)}

xy(santa)
xy(robot)

print coords
print len(coords)
