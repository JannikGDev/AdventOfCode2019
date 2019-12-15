from IntCode import IntCode
import numpy as np
import matplotlib.pyplot as plt
import math

NORTH = 1
SOUTH = 2
WEST = 3
EAST = 4

PATH_ID = 4
TARGET_ID = 3
ROBOT_ID = 2
WALL_ID = 1
EMPTY_ID = 0
UNKNOWN_ID = -1


def task15_1():
    data = read_input("input.txt")[0]
    code = [int(d) for d in data.split(',')]

    program = IntCode(code)
    status = -1
    steps = 0

    obs = np.ones((10, 10)) * (-1)

    robot_x = math.floor(obs.shape[0] * 0.5)
    robot_y = math.floor(obs.shape[1] * 0.5)

    start_x = robot_x
    start_y = robot_y

    obs[robot_x, robot_y] = 2

    while True:

        if min(abs(robot_x - obs.shape[0]), robot_x) < 10:
            n_obs = np.ones((obs.shape[0] * 2, obs.shape[1])) * -1
            offset = math.ceil(obs.shape[0] * 0.5)
            n_obs[offset:offset + obs.shape[0], :] = obs
            start_x = start_x + offset
            obs = n_obs
            robot_pos = np.where(obs == ROBOT_ID)
            robot_x = robot_pos[0][0]
            robot_y = robot_pos[1][0]

        if min(abs(robot_y - obs.shape[1]), robot_y) < 10:
            n_obs = np.ones((obs.shape[0], obs.shape[1] * 2)) * -1
            offset = math.ceil(obs.shape[1] * 0.5)
            n_obs[:, offset:offset + obs.shape[1]] = obs
            start_y = start_y + offset
            obs = n_obs
            robot_pos = np.where(obs == ROBOT_ID)
            robot_x = robot_pos[0][0]
            robot_y = robot_pos[1][0]

        move = repair_robot_step(obs)
        n_robot_y = robot_y
        n_robot_x = robot_x

        if move == NORTH:
            n_robot_y -= 1
        if move == WEST:
            n_robot_x -= 1
        if move == SOUTH:
            n_robot_y += 1
        if move == EAST:
            n_robot_x += 1

        program.run_until_output(input_values=[move])
        status = program.outputs.pop()

        if status == 0:
            obs[n_robot_x, n_robot_y] = WALL_ID
        if status == 1:
            obs[robot_x, robot_y] = EMPTY_ID
            obs[n_robot_x, n_robot_y] = ROBOT_ID
            robot_x = n_robot_x
            robot_y = n_robot_y
        if status == 2:
            obs[robot_x, robot_y] = EMPTY_ID
            obs[n_robot_x, n_robot_y] = TARGET_ID
            break

        steps += 1

        if steps % 100 == 0:
            print(steps)

        if steps % 10000 == 0:
            plt.imshow(obs.transpose())
            plt.show()

    def is_system(value):
        return value == TARGET_ID or value == ROBOT_ID

    print("STEPS: " + str(steps))

    path = djikstra(obs, [start_x, start_y], is_system, is_path)
    print("PATH_LEN: " + str(len(path)))

    for node in path:
        obs[node[0][0], node[0][1]] = PATH_ID


    plt.imshow(obs)
    plt.show()

    return

def task15_2():
    data = read_input("input.txt")[0]
    code = [int(d) for d in data.split(',')]

    program = IntCode(code)
    status = -1
    steps = 0

    obs = np.ones((10, 10)) * (-1)

    robot_x = math.floor(obs.shape[0] * 0.5)
    robot_y = math.floor(obs.shape[1] * 0.5)

    start_x = robot_x
    start_y = robot_y

    obs[robot_x, robot_y] = 2
    on_target = False

    while True:

        if min(abs(robot_x - obs.shape[0]), robot_x) < 10:
            n_obs = np.ones((obs.shape[0] * 2, obs.shape[1])) * -1
            offset = math.ceil(obs.shape[0] * 0.5)
            n_obs[offset:offset + obs.shape[0], :] = obs
            start_x = start_x + offset
            obs = n_obs
            robot_pos = np.where(obs == ROBOT_ID)
            robot_x = robot_pos[0][0]
            robot_y = robot_pos[1][0]

        if min(abs(robot_y - obs.shape[1]), robot_y) < 10:
            n_obs = np.ones((obs.shape[0], obs.shape[1] * 2)) * -1
            offset = math.ceil(obs.shape[1] * 0.5)
            n_obs[:, offset:offset + obs.shape[1]] = obs
            start_y = start_y + offset
            obs = n_obs
            robot_pos = np.where(obs == ROBOT_ID)
            robot_x = robot_pos[0][0]
            robot_y = robot_pos[1][0]

        move = repair_robot_step(obs)
        n_robot_y = robot_y
        n_robot_x = robot_x

        if move == NORTH:
            n_robot_y -= 1
        if move == WEST:
            n_robot_x -= 1
        if move == SOUTH:
            n_robot_y += 1
        if move == EAST:
            n_robot_x += 1
        if move is None:
            break

        program.run_until_output(input_values=[move])
        status = program.outputs.pop()

        if status == 0:
            obs[n_robot_x, n_robot_y] = WALL_ID
        if status == 1:
            if on_target:
                obs[robot_x, robot_y] = TARGET_ID
                on_target = False
            else:
                obs[robot_x, robot_y] = EMPTY_ID
            obs[n_robot_x, n_robot_y] = ROBOT_ID
            robot_x = n_robot_x
            robot_y = n_robot_y
        if status == 2:
            obs[robot_x, robot_y] = EMPTY_ID
            obs[n_robot_x, n_robot_y] = ROBOT_ID
            robot_x = n_robot_x
            robot_y = n_robot_y
            on_target = True

        steps += 1

        if steps % 100 == 0:
            print(steps)

        if steps % 10000 == 0:
            plt.imshow(obs.transpose())
            plt.show()

    def is_system(value):
        return value == TARGET_ID

    print("STEPS: " + str(steps))

    target_pos = np.where(obs == TARGET_ID)
    target_x = target_pos[0][0]
    target_y = target_pos[1][0]

    mins = floodfill(obs, [target_x, target_y], is_path)
    print("MINUTES: " + str(mins))

    path = djikstra(obs, [start_x, start_y], is_system, is_path)
    print("PATH_LEN: " + str(len(path)))

    for node in path:
        obs[node[0][0], node[0][1]] = PATH_ID

    plt.imshow(obs)
    plt.show()

    return


def repair_robot_step(obs):
    mypos = np.where(obs == ROBOT_ID)
    x = mypos[0][0]
    y = mypos[1][0]

    path = djikstra(obs, [x, y], is_target, is_path)
    if path is not None and len(path) > 0:
        next = path.pop()
        dx = next[0][0] - x
        dy = next[0][1] - y

        if dx == 1:
            return EAST
        if dx == -1:
            return WEST
        if dy == 1:
            return SOUTH
        if dy == -1:
            return NORTH

        assert False
    else:
        return None


def is_target(value):
    return value == UNKNOWN_ID


def is_path(value):
    return value == EMPTY_ID or value == ROBOT_ID


def djikstra(map, start_pos, is_target, is_path):
    start_node = make_node(start_pos, 0, None)

    queue = [start_node]
    visited_map = np.zeros(map.shape)

    end_node = None

    while len(queue) > 0:

        node = queue.pop(0)

        if visited_map[node[0][0], node[0][1]] == 1:
            continue

        visited_map[node[0][0], node[0][1]] = 1

        if is_target(map[node[0][0], node[0][1]]):
            end_node = node
            break

        for dir in [[0, 1], [0, -1], [1, 0], [-1, 0]]:

            new_x = node[0][0] + dir[0]
            new_y = node[0][1] + dir[1]

            if new_x < map.shape[0] and new_y < map.shape[1] and \
                    (is_path(map[new_x, new_y]) or is_target(map[new_x, new_y])):

                queue.append(make_node([new_x, new_y], node[1] + 1, node))

    if end_node is None:
        return None

    path = []
    current = end_node
    while current[2] is not None:
        path.append(current)
        current = current[2]

    return path


def floodfill(map, start_pos, is_path):
    start_node = make_node(start_pos, 0, None)

    queue = [start_node]
    visited_map = np.zeros(map.shape)

    end_node = None
    max_cost = 0

    while len(queue) > 0:

        node = queue.pop(0)

        if visited_map[node[0][0], node[0][1]] == 1:
            continue

        visited_map[node[0][0], node[0][1]] = 1

        if node[1] > max_cost:
            max_cost = node[1]

        for dir in [[0, 1], [0, -1], [1, 0], [-1, 0]]:

            new_x = node[0][0] + dir[0]
            new_y = node[0][1] + dir[1]

            if new_x < map.shape[0] and new_y < map.shape[1] and is_path(map[new_x, new_y]):
                queue.append(make_node([new_x, new_y], node[1] + 1, node))

    return max_cost


def make_node(position, cost, parent):
    return (position, cost, parent)


def read_input(path):
    input_data = []
    with open(path) as file:
        for line in file:
            input_data.append(line)

    return input_data


if __name__ == "__main__":
    task15_2()
