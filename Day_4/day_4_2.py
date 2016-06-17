import md5
word = raw_input()
print "Key: %s " % word
i = 0
while True:
    test = word + str(i)
    m = md5.new(test)
    test = m.hexdigest()
    if test[0:6:] == '000000':
        print "Number: %d " % i
        print "Hash: %s " % test
        break
    i += 1
