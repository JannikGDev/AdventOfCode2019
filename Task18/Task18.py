import numpy as np
from PQueue import PQueue
import matplotlib.pyplot as plt


START = ord("@")
WALL = ord("#")
EMPTY = ord(".")

def task18():

    data = read_input("input.txt")

    field = np.zeros((len(data[0]), len(data))).astype(np.int)

    for y, line in enumerate(data):
        for x, val in enumerate(line):
            if not val.isspace():
                field[x, y] = int(ord(val))

    display_map(field)

    field = remove_deadends(field)

    display_map(field)

    start_position = np.where(field == START)
    start_position = [start_position[0][0], start_position[1][0]]

    keys = []
    for x in range(len(field)):
        for y in range(len(field[x])):
            symbol = chr(field[x, y])
            if not symbol in ['#', '@', '.'] and symbol.islower():
                keys.append(chr(field[x, y]))

    no_keys = dict()

    for key in keys:
        no_keys[key] = False

    path_instances = [([], 0, None)]
    iterations = 0
    while True:
        n_path_instances = []

        if len(path_instances[0][0]) == len(keys):
            break

        for i, instance in enumerate(path_instances):

            for key in keys:

                if key in instance[0]:
                    continue

                key_position = np.where(field == ord(key))
                key_position = [key_position[0][0], key_position[1][0]]

                doors = [door.upper() for door in instance[0]]

                path = a_star(field, start_position, key_position, ['.', '@'] + doors + [key] + instance[0])

                if path is None:
                    continue

                steps = path[0][1]

                new_instance = (instance[0] + [key], instance[1] + steps, key)

                n_path_instances.append(new_instance)

        path_instances = strip_bad_instances(n_path_instances)
        iterations += 1
        print(iterations)

    for instance in path_instances:
        print(instance)

    return


def strip_bad_instances(instances):

    to_be_removed = []

    for i, A in enumerate(instances):
        for j, B in enumerate(instances):

            if i != j and A[2] == B[2] and equal_lists(A[0], B[0]):

                if A[1] > B[1]:
                    to_be_removed.append(i)
                    break

    for i in to_be_removed:
        del instances[i]

    return instances


def remove_deadends(field):
    change = True
    while change:

        change = False
        for x in range(1, len(field) - 1):
            for y in range(1, len(field[x]) - 1):
                if field[x, y] == ord('.'):
                    access = 0
                    if field[x + 1, y] != ord('#'):
                        access += 1
                    if field[x, y + 1] != ord('#'):
                        access += 1
                    if field[x - 1, y] != ord('#'):
                        access += 1
                    if field[x, y - 1] != ord('#'):
                        access += 1

                    if access <= 1:
                        field[x, y] = ord('#')
                        change = True

    return field


def display_map(field):

    plt.imshow(field)
    plt.show()


def equal_lists(A, B):

    dict_A = dict()
    dict_B = dict()

    for a in A:
        dict_A[a] = True
    for b in B:
        dict_B[b] = True

    return equal_dict(dict_A, dict_B)


def equal_dict(A, B):

    for key in A.keys():
        if not key in B:
            return False

    return True


def heuristic(A, B):

    dx = abs(A[0] - B[0])
    dy = abs(A[1] - B[1])

    return dx*dx+dy*dy


def a_star(field, start, end, allowed_symbols):

    q = PQueue()

    start_node = (
        start,
        0,
        None,
    )

    q.put(heuristic(start_node[0], end), start_node)
    visited_map = np.zeros(field.shape)

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

            if chr(field[x, y]) in allowed_symbols and visited_map[x, y] == 0:

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
