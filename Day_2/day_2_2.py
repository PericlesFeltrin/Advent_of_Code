total = 0
while True:
    try:
        l, w, h = raw_input().split('x')
    except EOFError:
        print ("Error: EOF or empty input!")
        break
    list = [int(l), int(w), int(h)]
    list.sort()
    total += (list[0] * list[1] * list[2]) + list[0] + list[0] + list[1] + list[1]
print total
