def def_AND(val1, val2):
    return val1 & val2

def def_OR(val1, val2):
    return val1 | val2

def def_RSHIFT(val1, val2):
    return val1 >> val2

def def_LSHIFT(val1, val2):
    return val1 << val2

def def_NOT(value):
    return 65535 - value

def change(array):
    for y in range(0, len(result), 2):
        for i, x in enumerate(array):
            if x == result[y]:
                array[i] = result[y+1]

def serch_def(val1, val2, op):
    x = '';
    if op == '&':
        x = def_AND(val1, val2)
    elif op == '|':
        x = def_OR(val1, val2)
    elif op == '>>':
        x = def_RSHIFT(val1, val2)
    elif op == '<<':
        x = def_LSHIFT(val1, val2)
    result.append(str(x))

def clear_array(array):
    for x in range(0, array.count('') ):
        array.remove('')

data = []
init = []
not_ = []
result = []
while True:
    try:
        string = raw_input()
    except EOFError:
        print ("Error: EOF or empty input!")
        break

    if 'AND' in string:
        string = string.replace(" AND ", " ")
        string = string.replace(" -> ", " ")
        d = string.split(' ')
        data.append(d[2])
        data.append(d[0])
        data.append('&')
        data.append(d[1])
    elif 'NOT' in string:
        string = string.replace("NOT ", "")
        d = string.split(' -> ')
        not_.append(d[1])
        not_.append(d[0])
    elif 'OR' in string:
        string = string.replace(" OR ", " ")
        string = string.replace(" -> ", " ")
        d = string.split(' ')
        data.append(d[2])
        data.append(d[0])
        data.append('|')
        data.append(d[1])
    elif 'RSHIFT' in string:
        string = string.replace(" RSHIFT ", " ")
        string = string.replace(" -> ", " ")
        d = string.split(' ')
        data.append(d[2])
        data.append(d[0])
        data.append('>>')
        data.append(d[1])
    elif 'LSHIFT' in string:
        string = string.replace(" LSHIFT ", " ")
        string = string.replace(" -> ", " ")
        d = string.split(' ')
        data.append(d[2])
        data.append(d[0])
        data.append('<<')
        data.append(d[1])
    else:
        d = string.split(' -> ')
        if d[0].isdigit():
            result.append(d[1])
            if d[1] == 'b':
                result.append('956')
            else:
                result.append((d[0]))
        else:
            init.append(d[1])
            init.append(d[0])

#print data
change(not_)
change(data)

while True:
    if (len(not_) == 0) & (len(data) == 0) & (len(init) == 0):
        break

    if len(data) != 0:
        change(data)
        for x in range(0, len(data), 4):
            if data[x+1].isdigit() & data[x+3].isdigit():
                result.append(data[x])
                serch_def(int(data[x+1]), int(data[x+3]), data[x+2])
                #print "%s = %s %s %s" % (data[x], data[x+1], data[x+2], data[x+3])
                data[x] = data[x+1] = data[x+2] = data[x+3] = ''
        clear_array(data)

    if len(not_) != 0:
        change(not_)
        for x in range(0, len(not_), 2):
            if not_[x+1].isdigit():
                result.append(not_[x])
                result.append(str(def_NOT(int(not_[x+1]))))
                #print "%s = NOT %s" % (not_[x], not_[x+1])
                not_[x] = not_[x+1] = ''
        clear_array(not_)

    if len(init) != 0:
        change(init)
        for x in range(0, len(init), 2):
            if init[x+1].isdigit():
                result.append(init[x])
                result.append(init[x+1])
                #print "%s -> %s" % (init[x], init[x+1])
                init[x] = init[x+1] = ''
        clear_array(init)

    if result.count('a'):
        #print result.index('a')
        break

print "All Results"
print result
print "a = %s" % result[result.index('a')+1]
