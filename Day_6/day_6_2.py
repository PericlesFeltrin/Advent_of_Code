def change_led(led, through, change):
    for x in range(int(led[0]), int(through[0])+1):
        for y in range(int(led[1]), int(through[1])+1):
            if (matrix[x][y] + change) > -1:
                matrix[x][y] += change

matrix = [ [ 0 for i in range(1000) ] for j in range(1000) ]
while True:
    try:
        string = raw_input()
    except EOFError:
        print ("Error: EOF or empty input!")
        break
    led = string.split(' through ')
    through = led[1].split(',')
    if "toggle" in led[0]:
        led = led[0][7::].split(",")
        change_led(led, through, 2)
    elif "turn on" in led[0]:
        led = led[0][8::].split(",")
        change_led(led, through, 1)
    elif "turn off" in led[0]:
        led = led[0][9::].split(",")
        change_led(led, through, -1)
led = 0
for x in range(0, 1000):
    led += sum(matrix[x])
print led
