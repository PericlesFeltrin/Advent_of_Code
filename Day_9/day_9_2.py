def next_city(here, new_route, cost):
    for x in range(0, len(routes_init), 3):
        new_route_copy = list(new_route)
        cost_copy = list(cost)
        if (routes_init[x] == here) & (routes_init[x+1] not in new_route_copy):
            new_route_copy.append(routes_init[x+1])
            cost_copy.append(routes_init[x+2])
            next_city(routes_init[x+1], new_route_copy, cost_copy)

    if len(new_route) == len(cities):
        new_route.append(sum(cost))
        routes_final.append(new_route)
    return

routes_init = []
cities = []
while True:
    try:
        string = raw_input()
    except EOFError:
        break

    value = string.split(" ")

    routes_init.append(value[0])
    routes_init.append(value[2])
    routes_init.append(int(value[4]))

    routes_init.append(value[2])
    routes_init.append(value[0])
    routes_init.append(int(value[4]))

    if value[0] not in cities:
        cities.append(value[0])
    if value[2] not in cities:
        cities.append(value[2])

routes_final = []
for x in range(0, len(routes_init), 3):
    new_route = []
    cost = []
    new_route.append(routes_init[x])
    new_route.append(routes_init[x+1])
    cost.append(routes_init[x+2])
    next_city(routes_init[x+1], new_route, cost)

print "Cities: "
print len(cities)

higth_cost = routes_final[0][-1]
print "Routes:"
for x in routes_final:
    print ' -> '.join(x[0:len(x)-1:]),
    print '= %d' % x[-1]
    if higth_cost < x[-1]:
        higth_cost = x[-1]

print "Higth Cost: %d" % higth_cost
