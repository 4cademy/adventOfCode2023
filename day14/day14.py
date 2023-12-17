import copy


def load_data():
    data = []
    with open('rocks') as f:
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
    # for line in data:
    #    print(line)
    # print('Tilting north')
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
    # for line in data:
    #     print(line)
    # print('Tilting west')
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
    # for line in data:
    #    print(line)
    # print('Tilting south')
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
    # for line in data:
    #     print(line)
    # print('Tilting east')
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
    # for line in data:
    #     print(line)
    # print('------------------')


def matrices_equal(mat1, mat2):
    for i, line in enumerate(mat1):
        for j, char in enumerate(line):
            if char != mat2[i][j]:
                return False
    return True


def matching_matrix(mat_list, mat2):
    match = False

    i = 0
    for i, mat in enumerate(mat_list):
        if matrices_equal(mat, mat2):
            match = True
            break
    return match, i


def find_loop(data):
    matrices = [copy.deepcopy(data)]
    steps = 0
    stop = False
    offset = 0
    while not stop:
        # print(f'Step {steps+1}:')
        tilt360(data)
        stop, offset = matching_matrix(matrices, data)
        matrices.append(copy.deepcopy(data))
        steps += 1
        # for mat in matrices:
        #    for line in mat:
        #        print(line)
        #    print()

    loop_length = steps-offset
    return offset, loop_length, matrices


def calc_after_one_billion(matrix_history, offset, loop_length):
    steps = 1000000000
    steps = steps - offset
    steps = steps % loop_length
    return matrix_history[offset + steps]


def task1(data):
    total = 0
    tilt_north(data)
    for i, line in enumerate(data):
        rocks = line.count('O')
        total += rocks * (len(data) - i)
    return total


def task2(data):
    total = 0
    offset, loop_length, matrix_history = find_loop(data)
    print(offset, loop_length)
    matrix = calc_after_one_billion(matrix_history, offset, loop_length)
    for i, line in enumerate(matrix):
        rocks = line.count('O')
        total += rocks * (len(matrix) - i)
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
