import numpy as np
import math

def task10_2():
    data = read_input("input.txt")
    data = [line.strip() for line in data]

    asteroid_map = parse_map(data)

    station_pos = task10_1()

    asteroid_map[station_pos[0], station_pos[1]] = 0

    targets = get_observed(station_pos, asteroid_map)

    angles = {}
    angles_list = []

    for target in targets:
        angle = get_angle(station_pos, target)
        angles[angle] = target
        angles_list.append(angle)

    angles_list.sort()

    final = angles[angles_list[199]]

    print(final)

    return


def get_angle(start,end):

    dx = end[0] - start[0]
    dy = end[1] - start[1]

    return ((math.atan2(dy, dx)*180/math.pi)+90+360) % 360


def task10_1():
    data = read_input("input.txt")
    data = [line.strip() for line in data]

    asteroid_map = parse_map(data)

    observations_map = create_observation_map(asteroid_map)

    best = np.max(observations_map)

    print(best)
    best_spot = np.unravel_index(np.argmax(observations_map, axis=None), observations_map.shape)

    return np.array([best_spot[0], best_spot[1]])


def create_observation_map(asteroid_map: np.ndarray):

    observations_map = np.zeros(asteroid_map.shape)

    asteroids = np.where(asteroid_map == 1)
    asteroids = [np.array([x_pos, y_pos]) for x_pos, y_pos in zip(asteroids[0], asteroids[1])]

    for i, observer in enumerate(asteroids):
        observations = 0
        for j, observed in enumerate(asteroids):
            if i != j:
                step = get_step_size(observer, observed)

                current = observer + step
                while True:
                    if current[0] == observed[0] and current[1] == observed[1]:
                        observations += 1
                        break

                    if asteroid_map[current[0], current[1]] == 1:
                        break

                    current = current + step

        observations_map[observer[0], observer[1]] = observations

    return observations_map

def get_observed(observer, asteroid_map):
    observations = []

    asteroids = np.where(asteroid_map == 1)
    asteroids = [np.array([x_pos, y_pos]) for x_pos, y_pos in zip(asteroids[0], asteroids[1])]

    for j, observed in enumerate(asteroids):
        if observer[0] != observed[0] or observer[1] != observed[1]:
            step = get_step_size(observer, observed)

            current = observer + step
            while True:
                if current[0] == observed[0] and current[1] == observed[1]:
                    observations.append(observed)
                    break

                if asteroid_map[current[0], current[1]] == 1:
                    break

                current = current + step

    return observations


def parse_map(data):

    asteroid_map = np.zeros((len(data[0]), len(data)))

    for y,line in enumerate(data):
        for x,spot in enumerate(line):
            if spot == "#":
                asteroid_map[x, y] = 1

    return asteroid_map.astype(np.uint8)


def get_step_size(observer, observed):
    dx = observed[0] - observer[0]
    dy = observed[1] - observer[1]

    if dx == 0:
        return [0, dy//abs(dy)]

    if dy == 0:
        return [dx//abs(dx),0]

    denominator = 1
    for i in range(2, min(abs(dx), abs(dy))+1):

        if abs(dx) % i == 0 and abs(dy) % i == 0:
            denominator = i

    step_x = dx // denominator
    step_y = dy // denominator

    return [step_x, step_y]

def read_input(path):

    input_data = []
    with open(path) as file:
        for line in file:
            input_data.append(line)

    return input_data




if __name__ == "__main__":
    task10_2()


