char_total = 0
result = 0
while True:
    try:
        string = raw_input()
    except EOFError:
        print ("Error: EOF or empty input!")
        break

    char_total += len(string)
    backslash = string.count("\\\\")*2
    string = string.replace("\\\\", '  ')
    result += string.count("\"")*2 + string.count("\\x") + backslash

print "Total Caractere: %d" % char_total
print "Total Caractere Encode: %d" % (char_total + result)
print "Caractere Encode - Caractere: %d" % result
