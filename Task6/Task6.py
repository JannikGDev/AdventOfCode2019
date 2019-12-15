

def task6():

    data = read_input("input.txt")

    orbits = [pair.strip().split(')') for pair in data]

    planets = {}

    root = 'COM'

    for orbit in orbits:

        left = orbit[0]
        right = orbit[1]

        planets[right] = left


    orbit_sum = 0
    for key in planets.keys():

        current = key

        while current in planets:
            current = planets[current]
            orbit_sum += 1

    print(orbit_sum)

def task6_2():
    data = read_input("input.txt")

    orbits = [pair.strip().split(')') for pair in data]

    planets = {}

    root = 'COM'

    you = 'YOU'
    san = 'SAN'

    for orbit in orbits:
        left = orbit[0]
        right = orbit[1]

        planets[right] = left

    path_you = []
    path_san = []

    current = 'YOU'
    cost = 0
    while current in planets:
        current = planets[current]
        path_you.append((current, cost))
        cost += 1

    current = 'SAN'
    cost = 0
    while current in planets:
        current = planets[current]
        path_san.append((current, cost))
        cost += 1

    for you_node in path_you:
        for san_node in path_san:

            if you_node[0] == san_node[0]:
                print(you_node[1]+san_node[1])
                return

def read_input(path):

    input_data = []
    with open(path) as file:
        for line in file:
            input_data.append(line)

    return input_data


if __name__ == "__main__":
    task6_2()
