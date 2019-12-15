

def task3():

    data = read_input("input.txt")

    data_A = data[0].strip().split(",")
    data_B = data[1].strip().split(",")

    path_A = parse_path(data_A)
    path_B = parse_path(data_B)

    intersections = find_intersections(path_A, path_B)

    closest = find_min_manhattan(intersections)
    print(intersections)
    distances = [intersection_distance(path_A, path_B, inter) for inter in intersections]
    distances = [d[0]+d[1] for d in distances]

    print(min(distances))


def intersection_distance(path_a, path_b, intersection):

    steps_a = 0
    for i in range(len(path_a)-1):

        x0 = min(path_a[i][0], path_a[i + 1][0])
        y0 = min(path_a[i][1], path_a[i + 1][1])
        x1 = max(path_a[i][0], path_a[i + 1][0])
        y1 = max(path_a[i][1], path_a[i + 1][1])

        ix = intersection[0]
        iy = intersection[1]

        if (x0 < ix and x1 > ix and y0 == iy == y1) or (y0 < iy and y1 > iy and x0 == x1 == ix):

            steps_a += abs(ix - path_a[i][0]) + abs(iy - path_a[i][1])
            break

        steps_a += abs(x1 - x0) + abs(y1 - y0)

    steps_b = 0
    for i in range(len(path_b)-1):

        x0 = min(path_b[i][0], path_b[i + 1][0])
        y0 = min(path_b[i][1], path_b[i + 1][1])
        x1 = max(path_b[i][0], path_b[i + 1][0])
        y1 = max(path_b[i][1], path_b[i + 1][1])

        ix = intersection[0]
        iy = intersection[1]

        if (x0 < ix and x1 > ix and y0 == iy == y1) or (y0 < iy and y1 > iy and x0 == x1 == ix):

            steps_b += abs(ix - path_b[i][0]) + abs(iy - path_b[i][1])
            break

        steps_b += abs(x1 - x0) + abs(y1 - y0)

    return steps_a, steps_b


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

            if a_horizontal and not b_horizontal:

                if by0 <= ay0 and by1 >= ay0 and ax0 <= bx0 and ax1 >= bx1:
                    intersections.append((bx1, ay0))

            elif b_horizontal and not a_horizontal:

                if ay0 <= by0 and ay1 >= by0 and bx0 <= ax0 and bx1 >= ax1:
                    intersections.append((ax1, by0))

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