import re
nice_strings = []
while True:
    try:
        string = raw_input()
    except EOFError:
        print ("Error: EOF or empty input!")
        break
    if string == '':
        break
    repeat = re.search(r"([a-z]{2,}?).*\1", string)
    if repeat != None:
        double = re.search(r"([a-z]).\1", string)
        if double != None:
            nice_strings.append(string)

print len(nice_strings)
print nice_strings
