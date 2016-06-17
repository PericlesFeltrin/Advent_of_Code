total = 0
while True:
    try:
        l, w, h = raw_input().split('x')
    except EOFError:
        print ("Error: EOF or empty input!")
        break
    list = [(int(l)*int(w)), (int(w)*int(h)), (int(h)*int(l))]
    total += 2*list[0] + 2*list[1] + 2*list[2]
    list.sort()
    total += list[0]
print total
