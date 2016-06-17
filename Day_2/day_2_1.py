total = 0
while True:
    try:
        l, w, h = raw_input().split('x')
    except EOFError:
        print ("Error: EOF or empty input!")
        break
    l = int(l)
    w = int(w)
    h = int(h)
    list = [(l*w), (w*h), (h*l)]
    total += 2*list[0] + 2*list[1] + 2*list[2]
    list.sort()
    total += list[0]
print total
