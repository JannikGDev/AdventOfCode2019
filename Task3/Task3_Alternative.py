

def task3():

    data = read_input("input.txt")

    data_A = data[0].strip().split(",")
    data_B = data[1].strip().split(",")

    path_A = parse_path(data_A)
    path_B = parse_path(data_B)

    intersections = find_intersections(path_A, path_B)[1:]

    distances_a = [intersection_distance(data_A, x) for x in intersections]
    distances_b = [intersection_distance(data_B, x) for x in intersections]

    distances_sum = [da + db for (da,db) in zip(distances_a,distances_b)]

    print(min(distances_sum))


def intersection_distance(data, intersection):

    distance_a = 0
    x = 0
    y = 0
    for move in data:

        direction = move[0]
        length = int(move[1:])

        for i in range(length):

            distance_a += 1

            if direction == 'R':
                x += 1
            elif direction == 'L':
                x -= 1
            elif direction == 'U':
                y -= 1
            elif direction == 'D':
                y += 1

            if x == intersection[0] and y == intersection[1]:
                return distance_a

    return None

def parse_path(data):
    x = 0
    y = 0
    path = [(0, 0)]

    for move in data:

        dir = move[0]
        steps = int(move[1:])

        if dir == 'U':
            y -= steps
            path.append((x, y))
        elif dir == 'R':
            x += steps
            path.append((x, y))
        elif dir == 'L':
            x -= steps
            path.append((x, y))
        elif dir == 'D':
            y += steps
            path.append((x, y))

    return path


def find_intersections(path_A, path_B):

    intersections = []

    for i in range(len(path_A)-1):
        for j in range(len(path_B)-1):
            move_a = (path_A[i], path_A[i+1])
            move_b = (path_B[j], path_B[j + 1])

            ax0 = min(path_A[i][0], path_A[i+1][0])
            ay0 = min(path_A[i][1], path_A[i+1][1])
            ax1 = max(path_A[i][0], path_A[i+1][0])
            ay1 = max(path_A[i][1], path_A[i+1][1])
            a_horizontal = ay0 == ay1

            bx0 = min(path_B[j][0], path_B[j+1][0])
            by0 = min(path_B[j][1], path_B[j+1][1])
            bx1 = max(path_B[j][0], path_B[j+1][0])
            by1 = max(path_B[j][1], path_B[j+1][1])
            b_horizontal = by0 == by1

            if not (move_a[0][0] == move_a[0][1] == 0 == move_b[0][0] == move_b[0][1]):

                if a_horizontal and not b_horizontal:

                    if by0 <= ay0 and by1 >= ay0 and ax0 <= bx0 and ax1 >= bx1:
                        intersections.append((bx1, ay0))

                elif b_horizontal and not a_horizontal:

                    if ay0 <= by0 and ay1 >= by0 and bx0 <= ax0 and bx1 >= ax1:
                        intersections.append((ax1, by0))

                elif a_horizontal and b_horizontal:
                    if ay0 == by0 and (not (bx1 < ax0 or ax1 < bx0)):
                        raise ValueError("NOPE")

                elif not a_horizontal and not b_horizontal:
                    if ax1 == bx1 and (not (by1 < ay0 or ay1 < by0)):
                        raise ValueError("NOPE")

    return intersections


def find_min_manhattan(points):

    min_dis = None
    min_point = None

    for point in points:
        dis = abs(point[0])+abs(point[1])
        if (min_point is None or dis < min_dis) and dis > 0:
            min_dis = dis
            min_point = point

    return min_point


def read_input(path):

    input_data = []
    with open(path) as file:
        for line in file:
            input_data.append(line)

    return input_data


if __name__ == "__main__":
    task3()