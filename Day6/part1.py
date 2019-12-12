from collections import defaultdict

def dfs(orbit, orbit_map, orbits):
    current_value = orbits
    for o in orbit_map[orbit]:
        current_value += dfs(o, orbit_map, orbits + 1)
    return current_value

def compute_orbits():
    line = input()
    orbited, orbiting =  line.split(')')
    orbit_map = defaultdict(list)

    while line:
        orbit_map[orbited].append(orbiting)
        line = input()
        if line:
            orbited, orbiting =  line.split(')')

    return dfs("COM", orbit_map, 0)

print(compute_orbits())