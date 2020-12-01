from collections import defaultdict

def dfs(orbit, orbit_map, orbits, distance_to, SAN=False):
    if orbit == "COM":
        return
    for o in orbit_map[orbit]:
        if SAN and distance_to[o]:
            return orbits + distance_to[o]
        distance_to[o] = orbits
        return dfs(o, orbit_map, orbits + 1, distance_to, SAN)

def compute_orbits():
    line = input()
    orbited, orbiting =  line.split(')')
    orbit_map = defaultdict(list)
    distance_to = defaultdict(int)

    while line:
        orbit_map[orbiting].append(orbited)
        line = input()
        if line:
            orbited, orbiting =  line.split(')')

    if orbit_map["YOU"][0] == orbit_map["SAN"][0]:
        return 0
    dfs("YOU", orbit_map, 0, distance_to)
    return dfs("SAN", orbit_map, 0, distance_to, True)

print(compute_orbits())