def change_led(led, through, change):
    for x in range(int(led[0]), int(through[0])+1):
        for y in range(int(led[1]), int(through[1])+1):
            matrix[x][y] = change

def toggle_led(led, through):
    for x in range(int(led[0]), int(through[0])+1):
        for y in range(int(led[1]), int(through[1])+1):
            if matrix[x][y] == 1:
                matrix[x][y] = 0
            else:
                matrix[x][y] = 1

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
        toggle_led(led, through)
    elif "turn on" in led[0]:
        led = led[0][8::].split(",")
        change_led(led, through, 1)
    elif "turn off" in led[0]:
        led = led[0][9::].split(",")
        change_led(led, through, 0)
led = 0
for x in range(0, 1000):
    led += matrix[x].count(1)
print led
