char_total = 0
result = 0
while True:
    try:
        string = raw_input()
    except EOFError:
        print ("Error: EOF or empty input!")
        break

    char_total += len(string)
    backslash = string.count("\\\\")
    string = string.replace("\\\\", '')
    result += string.count("\"") + backslash + (string.count("\\x")*3)

print "Total Caractere: %d" % char_total
print "Total Caractere in Memory: %d" % (char_total - result)
print "Caractere - Caractere in Memory: %d" % result
