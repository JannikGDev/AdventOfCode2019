import numpy as np
from PQueue import PQueue


START = ord("@")
WALL = ord("#")
EMPTY = ord(".")


def task18():

    data = read_input("input.txt")

    map = np.zeros((len(data[0]), len(data))).astype(np.int)

    for y, line in enumerate(data):
        for x, val in enumerate(line):
            if not val.isspace():
                map[x, y] = int(ord(val))

    start_position = np.where(map == START)
    start_position = [start_position[0][0], start_position[1][0]]

    keys = []
    for x in range(len(map)):
        for y in range(len(map[x])):
            symbol = chr(map[x, y])
            if not symbol in ['#', '@', '.'] and symbol.islower():
                keys.append(chr(map[x, y]))

    path_instances = [([], 0)]
    while True:
        if len(path_instances[0][0]) == len(keys):
            break

        for i, instance in enumerate(path_instances):

            for key in keys:

                if key in instance[0]:
                    continue

                key_position = np.where(map == ord(key))
                key_position = [key_position[0][0], key_position[1][0]]

                doors = [door.upper() for door in instance[0]]

                path = a_star(map, start_position, key_position, ['.','@'] + doors + [key] + instance[0])

                if path is None:
                    continue

                steps = path[0][1]

                new_instance = (instance[0] + [key], instance[1]+steps)

                del path_instances[i]
                path_instances.append(new_instance)


    for instance in path_instances:
        print(instance)

    return


def heuristic(A, B):

    dx = abs(A[0] - B[0])
    dy = abs(A[1] - B[1])

    return dx*dx+dy*dy


def a_star(map, start, end, allowed_symbols):

    q = PQueue()

    start_node = (
        start,
        0,
        None,
    )

    q.put(heuristic(start_node[0], end), start_node)
    visited_map = np.zeros(map.shape)

    end_node = None

    while not q.empty():

        node = q.get()

        if visited_map[node[0][0], node[0][1]] == 1:
            continue
        else:
            visited_map[node[0][0], node[0][1]] = 1

        if node[0][0] == end[0] and node[0][1] == end[1]:
            end_node = node
            break


        for move in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
            x = node[0][0]+move[0]
            y = node[0][1]+move[1]

            if chr(map[x, y]) in allowed_symbols and visited_map[x, y] == 0:

                next_node = (
                    [x, y],
                    node[1]+1,
                    node
                )

                q.put(heuristic(next_node[0], end), next_node)

    if end_node is None:
        return None


    path = []
    current = end_node
    while not current[2] is None:
        path.append(current)
        current = current[2]

    return path

def read_input(path):

    input_data = []
    with open(path) as file:
        for line in file:
            input_data.append(line.strip())

    return input_data


if __name__ == "__main__":
    task18()
