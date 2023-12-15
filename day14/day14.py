import copy


def load_data():
    data = []
    with open('rocks_test1') as f:
        for line in f.readlines():
            line_array = []
            for char in line.strip():
                line_array.append(char)
            data.append(line_array)
    return data


def tilt_north(data):
    changed = True
    while changed:
        changed = False
        for i, line in enumerate(data):
            if i != 0:
                for j, char in enumerate(line):
                    if char == 'O':
                        if data[i-1][j] == '.':
                            data[i-1][j] = 'O'
                            data[i][j] = '.'
                            changed = True


def tilt360(data):
    changed = True
    while changed:
        changed = False
        for i, line in enumerate(data):
            if i != 0:
                for j, char in enumerate(line):
                    if char == 'O':
                        if data[i - 1][j] == '.':
                            data[i - 1][j] = 'O'
                            data[i][j] = '.'
                            changed = True
    changed = True
    while changed:
        changed = False
        for i, line in enumerate(data):
            for j, char in enumerate(line):
                if j != 0:
                    if char == 'O':
                        if data[i][j - 1] == '.':
                            data[i][j - 1] = 'O'
                            data[i][j] = '.'
                            changed = True
    changed = True
    while changed:
        changed = False
        for i, line in enumerate(data):
            if i != len(data) - 1:
                for j, char in enumerate(line):
                    if char == 'O':
                        if data[i + 1][j] == '.':
                            data[i + 1][j] = 'O'
                            data[i][j] = '.'
                            changed = True
    changed = True
    while changed:
        changed = False
        for i, line in enumerate(data):
            for j, char in enumerate(line):
                if j != len(line) - 1:
                    if char == 'O':
                        if data[i][j+1] == '.':
                            data[i][j+1] = 'O'
                            data[i][j] = '.'
                            changed = True


def matrices_equal(mat1, mat2):
    for i, line in enumerate(mat1):
        for j, char in enumerate(line):
            if char != mat2[i][j]:
                return False
    return True


def matching_matrix(mat_list, mat2):
    match = False
    for i, mat in enumerate(mat_list):
        if matrices_equal(mat, mat2):
            match = True
            break
    return match, i


def find_loop(data):
    matrices = [copy.deepcopy(data)]
    tilt360(data)
    steps = 1
    stop, offset = matching_matrix(matrices, data)
    while not stop:
        print(f'Step {steps}')
        tilt360(data)
        matrices.append(copy.deepcopy(data))
        steps += 1
        stop, i = matching_matrix(matrices, data)
    loop_length = steps-offset
    return loop_length, offset


def task1(data):
    total = 0
    tilt_north(data)
    for i, line in enumerate(data):
        rocks = line.count('O')
        total += rocks * (len(data) - i)
    return total


def task2(data):
    total = 0
    loop_length, offset = find_loop(data)
    print(loop_length, offset)
    return total


def main():
    data = load_data()
    for line in data:
        print(line)
    print()

    print(f'Task 1: {task1(data)}')
    print(f'Task 2: {task2(data)}')


if __name__ == '__main__':
    main()
