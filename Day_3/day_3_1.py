coord_input = list(raw_input())
x = 0
y = 0
coords = {(0,0)}
for xy in coord_input:
    if xy == '^':
        x += 1
    elif xy == 'v':
        x -= 1
    elif xy == '>':
        y += 1
    elif xy == '<':
        y -= 1
    coords.add((x,y))
print coords
print len(coords)
