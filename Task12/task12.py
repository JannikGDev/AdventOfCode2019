import numpy as np
import math

def task12_1(cycles):

    data = read_input("input.txt")

    moons = []

    for line in data:
        moon = dict()
        moon['x'] = 0
        moon['y'] = 0
        moon['z'] = 0
        moon['vx'] = 0
        moon['vy'] = 0
        moon['vz'] = 0

        line_data = line.strip()[1:-1]
        entries = line_data.split(',')
        moon['x'] = int(entries[0].strip()[2:])
        moon['y'] = int(entries[1].strip()[2:])
        moon['z'] = int(entries[2].strip()[2:])

        moons.append(moon)

    for i in range(cycles):
        moons = apply_gravity_step(moons)
        moons = apply_velocity(moons)

    print_moons(moons)


def task12_2():
    data = read_input("input.txt")

    moons = []

    for line in data:
        moon = dict()
        moon['x'] = 0
        moon['y'] = 0
        moon['z'] = 0
        moon['vx'] = 0
        moon['vy'] = 0
        moon['vz'] = 0

        line_data = line.strip()[1:-1]
        entries = line_data.split(',')
        moon['x'] = int(entries[0].strip()[2:])
        moon['y'] = int(entries[1].strip()[2:])
        moon['z'] = int(entries[2].strip()[2:])

        moons.append(moon)

    x_state = np.zeros(shape=len(moons))
    y_state = np.zeros(shape=len(moons))
    z_state = np.zeros(shape=len(moons))

    for i,moon in enumerate(moons):
        x_state[i] = moon['x']
        y_state[i] = moon['y']
        z_state[i] = moon['z']

    x_cycles = calc_sytem_cycle(x_state)
    y_cycles = calc_sytem_cycle(y_state)
    z_cycles = calc_sytem_cycle(z_state)

    task12_1(x_cycles)
    task12_1(y_cycles)
    task12_1(z_cycles)

    def lcm(a, b):
        return abs(a * b) // math.gcd(a, b)

    cycles = lcm(lcm(x_cycles, y_cycles), z_cycles)

    print(cycles)

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

def calc_sytem_cycle(start_state: np.ndarray):

    state = start_state.copy()
    velocity = np.zeros(state.shape)
    cycles = 0

    while True:
        cycles += 1
        for i in range(len(start_state)):
            higher = len(np.where(state > state[i])[0])
            lower = len(np.where(state < state[i])[0])
            velocity[i] += higher - lower

        state += velocity

        if np.equal(state, start_state).min() and np.all(velocity == 0):
            return cycles


def print_moons(moons):

    for moon in moons:
        print(moon)

def calc_total_energy_np(state, velocity):

    return state.sum()*velocity.sum()

def calc_total_energy(moons):

    energy = 0

    for moon in moons:
        energy += calc_moon_energy(moon)

    return energy

def calc_moon_energy(moon):

    pot = abs(moon['vx'])+abs(moon['vy'])+abs(moon['vz'])
    kin = abs(moon['x']) + abs(moon['y']) + abs(moon['z'])

    return pot*kin


def apply_gravity_step(moons):

    pairs = [(A, B) for A in moons for B in moons]

    pairs = filter(lambda pair: pair[0] != pair[1], pairs)
    pairs = [pair for pair in pairs]

    for pair in pairs:
        A = pair[0]
        B = pair[1]

        dx = B['x'] - A['x']
        dy = B['y'] - A['y']
        dz = B['z'] - A['z']

        if dx != 0:
            A['vx'] += dx / abs(dx)

        if dy != 0:
            A['vy'] += dy / abs(dy)

        if dz != 0:
            A['vz'] += dz / abs(dz)

    return moons


def apply_velocity(moons):

    for moon in moons:

        moon['x'] += moon['vx']
        moon['y'] += moon['vy']
        moon['z'] += moon['vz']

    return moons


def read_input(path):

    input_data = []
    with open(path) as file:
        for line in file:
            input_data.append(line)

    return input_data


if __name__ == "__main__":
    task12_2()
