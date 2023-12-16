import copy

checked_mirrors = []


def load_data():
    data = []
    with open('mirrors') as f:
        for line in f.readlines():
            line_array = []
            for char in line.strip():
                line_array.append(char)
            data.append(line_array)
    return data


def move_through(data, output, start, direction):
    global checked_mirrors
    print()
    for line in output:
        print(line)

    y, x = start
    next_pos = None
    if direction == 'up':
        next_pos = (y-1, x)
    elif direction == 'down':
        next_pos = (y+1, x)
    elif direction == 'left':
        next_pos = (y, x-1)
    elif direction == 'right':
        next_pos = (y, x+1)
    else:
        raise ValueError(f'Unknown direction: {direction}')

    if next_pos[0] < 0 or next_pos[0] >= len(data) or next_pos[1] < 0 or next_pos[1] >= len(data[0]):
        return

    next_char = data[next_pos[0]][next_pos[1]]
    output[next_pos[0]][next_pos[1]] = '#'
    while next_char == '.':
        if direction == 'up':
            next_pos = (next_pos[0]-1, next_pos[1])
        elif direction == 'down':
            next_pos = (next_pos[0]+1, next_pos[1])
        elif direction == 'left':
            next_pos = (next_pos[0], next_pos[1]-1)
        elif direction == 'right':
            next_pos = (next_pos[0], next_pos[1]+1)
        if next_pos[0] < 0 or next_pos[0] >= len(data) or next_pos[1] < 0 or next_pos[1] >= len(data[0]):
            return
        next_char = data[next_pos[0]][next_pos[1]]
        output[next_pos[0]][next_pos[1]] = '#'

    print(checked_mirrors)
    if tuple([next_pos, direction]) in checked_mirrors:
        return

    if next_char == '/':
        checked_mirrors.append(tuple([next_pos, direction]))
        if direction == 'up':
            move_through(data, output, next_pos, 'right')
        elif direction == 'down':
            move_through(data, output, next_pos, 'left')
        elif direction == 'left':
            move_through(data, output, next_pos, 'down')
        elif direction == 'right':
            move_through(data, output, next_pos, 'up')
        else:
            raise ValueError(f'Unknown direction: {direction}')
    elif next_char == '\\':
        checked_mirrors.append(tuple([next_pos, direction]))
        if direction == 'up':
            move_through(data, output, next_pos, 'left')
        elif direction == 'down':
            move_through(data, output, next_pos, 'right')
        elif direction == 'left':
            move_through(data, output, next_pos, 'up')
        elif direction == 'right':
            move_through(data, output, next_pos, 'down')
        else:
            raise ValueError(f'Unknown direction: {direction}')
    elif next_char == '|':
        checked_mirrors.append(tuple([next_pos, direction]))
        if direction == 'up':
            move_through(data, output, next_pos, 'up')
        elif direction == 'down':
            move_through(data, output, next_pos, 'down')
        elif direction == 'left' or direction == 'right':
            move_through(data, output, next_pos, 'up')
            move_through(data, output, next_pos, 'down')
        else:
            raise ValueError(f'Unknown direction: {direction}')
    elif next_char == '-':
        checked_mirrors.append(tuple([next_pos, direction]))
        if direction == 'up' or direction == 'down':
            move_through(data, output, next_pos, 'left')
            move_through(data, output, next_pos, 'right')
        elif direction == 'left':
            move_through(data, output, next_pos, 'left')
        elif direction == 'right':
            move_through(data, output, next_pos, 'right')
        else:
            raise ValueError(f'Unknown direction: {direction}')


def task1(data):
    total = 0
    output = []
    for line in data:
        line_array = []
        for char in line:
            line_array.append('.')
        output.append(line_array)

    move_through(data, output, (0, -1), 'right')

    for line in output:
        total += line.count('#')

    return total


def task2(data):
    total = 0
    return total


def main():
    data = load_data()
    for line in data:
        print(line)
    print()

    print(f'Task 1: {task1(copy.deepcopy(data))}')
    print(f'Task 2: {task2(copy.deepcopy(data))}')


if __name__ == '__main__':
    main()
