def load_data():
    data = []
    with open('pipes') as f:
        for line in f.readlines():
            line = line.strip()
            data.append(line)
    return data


def find_start(data):
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == 'S':
                return x, y


def get_start_directions(data, x, y):
    directions = []
    # north
    if y > 0 and data[y - 1][x] in '|7F':
        directions.append('north')
    # south
    if y < len(data) and data[y + 1][x] in '|LJ':
        directions.append('south')
    # west
    if x > 0 and data[y][x - 1] in '-LF':
        directions.append('west')
    # east
    if x < len(data[y]) and data[y][x + 1] in '-J7':
        directions.append('east')
    return directions


def get_next_direction(data, x, y, incomming_direction):
    if incomming_direction == 'north':
        if data[y][x] == '|':
            return 'south'
        elif data[y][x] == 'L':
            return 'east'
        elif data[y][x] == 'J':
            return 'west'
        else:
            raise ValueError(f'Unknown direction: {incomming_direction} for {data[y][x]}')
    elif incomming_direction == 'south':
        if data[y][x] == '|':
            return 'north'
        elif data[y][x] == 'F':
            return 'east'
        elif data[y][x] == '7':
            return 'west'
        else:
            raise ValueError(f'Unknown direction: {incomming_direction} for {data[y][x]}')
    elif incomming_direction == 'west':
        if data[y][x] == '-':
            return 'east'
        elif data[y][x] == '7':
            return 'south'
        elif data[y][x] == 'J':
            return 'north'
        else:
            raise ValueError(f'Unknown direction: {incomming_direction} for {data[y][x]}')
    elif incomming_direction == 'east':
        if data[y][x] == '-':
            return 'west'
        elif data[y][x] == 'F':
            return 'south'
        elif data[y][x] == 'L':
            return 'north'
        else:
            raise ValueError(f'Unknown direction: {incomming_direction} for {data[y][x]}')
    else:
        raise ValueError(f'Unknown direction: {incomming_direction} for {data[y][x]}')


def opposite_direction(direction):
    if direction == 'north':
        return 'south'
    elif direction == 'south':
        return 'north'
    elif direction == 'west':
        return 'east'
    elif direction == 'east':
        return 'west'


def get_loop_coordinates(data):
    coordinates = []
    x, y = find_start(data)
    next_direction = get_start_directions(data, x, y)[0]
    if next_direction == 'north':
        y -= 1
    elif next_direction == 'south':
        y += 1
    elif next_direction == 'west':
        x -= 1
    elif next_direction == 'east':
        x += 1
    coordinates.append((x, y))
    while data[y][x] != 'S':
        next_direction = get_next_direction(data, x, y, opposite_direction(next_direction))
        if next_direction == 'north':
            y -= 1
        elif next_direction == 'south':
            y += 1
        elif next_direction == 'west':
            x -= 1
        elif next_direction == 'east':
            x += 1
        coordinates.append((x, y))
    return coordinates


def set_char(string, char, index):
    return string[:index] + char + string[index+1:]


def fill_area_next_to_loop(data, coordinates):
    prev_x, prev_y = find_start(data)
    for x, y in coordinates:
        dif_x = x - prev_x
        dif_y = y - prev_y
        # went east
        if dif_x == 1:
            tmp = len(data)
            if y+1 < len(data):
                if (x, y+1) not in coordinates:
                    data[y+1] = set_char(data[y+1], '1', x)
                if (x-1, y+1) not in coordinates:
                    data[y+1] = set_char(data[y+1], '1', x-1)
        # went west
        if dif_x == -1:
            if y-1 >= 0:
                if (x, y-1) not in coordinates:
                    data[y-1] = set_char(data[y-1], '1', x)
                if (x+1, y-1) not in coordinates:
                    data[y-1] = set_char(data[y-1], '1', x+1)
        # went south
        if dif_y == 1:
            if x-1 >= 0:
                if (x-1, y) not in coordinates:
                    data[y] = set_char(data[y], '1', x-1)
                if (x-1, y-1) not in coordinates:
                    data[y-1] = set_char(data[y-1], '1', x-1)
        # went north
        if dif_y == -1:
            if x+1 < len(data[0]):
                if (x+1, y) not in coordinates:
                    data[y] = set_char(data[y], '1', x+1)
                if (x+1, y+1) not in coordinates:
                    data[y+1] = set_char(data[y+1], '1', x+1)
        prev_x = x
        prev_y = y
    return data


def spread_filling(data, coordinates):
    check_coordinates = []
    changed = True
    is_outer_filling = False
    while changed:
        changed = False
        for y in range(len(data)):
            for x in range(len(data[y])):
                tmp = data[y][x]
                tmp2 = (x, y)
                tmp3 = (x, y) not in check_coordinates
                if data[y][x] == '1' and ((x, y) not in check_coordinates):
                    for iter_y in range(y-1, y+2):
                        for iter_x in range(x-1, x+2):
                            if iter_x in range(len(data[0])) and iter_y in range(len(data)):
                                if (iter_x, iter_y) not in coordinates:
                                    data[iter_y] = set_char(data[iter_y], '1', iter_x)
                                    changed = True
                                    if iter_x == 0 or iter_x == len(data[0])-1 or iter_y == 0 or iter_y == len(data)-1:
                                        is_outer_filling = True
                    check_coordinates.append((x, y))
    return data, is_outer_filling


def task1(data):
    coordinates = get_loop_coordinates(data)
    return len(coordinates)/2


def count_filling(data):
    count = 0
    for line in data:
        for char in line:
            if char == '1':
                count += 1
    return count


def task2(data):
    coordinates = get_loop_coordinates(data)
    loop_length = len(coordinates)
    data = fill_area_next_to_loop(data, coordinates)
    filling_data = spread_filling(data, coordinates)
    is_outer_filling = filling_data[1]
    filling_count = count_filling(filling_data[0])
    if is_outer_filling:
        return len(data)*len(data[0]) - loop_length - filling_count
    else:
        return filling_count


def main():
    data = load_data()
    print(f'Task 1: {task1(data)}')
    print(f'Task 2: {task2(data)}')


if __name__ == '__main__':
    main()
