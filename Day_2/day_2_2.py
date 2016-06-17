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
    list = [l, w, h]
    list.sort()
    total += (list[0] * list[1] * list[2]) + list[0] + list[0] + list[1] + list[1]
print total
