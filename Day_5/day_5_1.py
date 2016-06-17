import re
nice_strings = []
while True:
    try:
        string = raw_input()
    except EOFError:
        print ("Error: EOF or empty input!")
        break

    not_in = re.search(r"(ab|cd|pq|xy)", string)
    if not_in == None:
        vowels = re.findall(r"[aeiou]", string)
        if len(vowels) >= 3:
            double = re.search(r"(.)\1", string)
            if double != None:
                nice_strings.append(string)

print len(nice_strings)
print nice_strings
