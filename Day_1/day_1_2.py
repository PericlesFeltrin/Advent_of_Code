str = raw_input()
open = 0
close = 0
pos = 1
for s in str:
    if s == '(':
        open += 1
    elif s == ')':
        close += 1
    if open < close:
        break;
    pos += 1
print pos
