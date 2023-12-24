import copy


def load_data():
    data = []
    with open('dig_plan') as f:
        for line in f.readlines():
            line = line.strip()
            line_array = []
            line_array = line.split(' ')
            line_array[1] = int(line_array[1])
            line_array[2] = line_array[2].replace('(', '')
            line_array[2] = line_array[2].replace('#', '')
            line_array[2] = line_array[2].replace(')', '')
            data.append(line_array)
    return data


def extract_from_hex(data):
    real_data = []
    for line in data:
        hex_value = int(line[2][0:5], 16)
        direction = line[2][5]
        if direction == '0':
            real_data.append(['R', hex_value])
        elif direction == '1':
            real_data.append(['D', hex_value])
        elif direction == '2':
            real_data.append(['L', hex_value])
        elif direction == '3':
            real_data.append(['U', hex_value])
    return real_data


def print_matrix(matrix):
    for row in matrix:
        for item in row:
            print(item, end='\t\t')
        print()


def make_corner_list(data):
    corner_list = [(0, 0)]
    for line in data:
        if line[0] == 'R':
            corner_list.append((corner_list[-1][0], corner_list[-1][1] + line[1]))
        elif line[0] == 'L':
            corner_list.append((corner_list[-1][0], corner_list[-1][1] - line[1]))
        elif line[0] == 'U':
            corner_list.append((corner_list[-1][0] - line[1], corner_list[-1][1]))
        elif line[0] == 'D':
            corner_list.append((corner_list[-1][0] + line[1], corner_list[-1][1]))
    return corner_list


def area_from_corners(corner_list, data):
    area = 0
    for i in range(len(corner_list) - 1):
        area += (corner_list[i][1]*corner_list[i+1][0] - corner_list[i+1][1]*corner_list[i][0])
    area = 0.5 * area
    # for four corners
    area += 3
    # for each line between corners
    for line in data:
        area += (line[1]-1)/2
    # for each corner except the four outer corners (which are already counted)
    # must subtract 5 because first corner twice in list
    area += (len(corner_list) - 5)/2
    return area


def task1(data):
    total = 0
    corner_list = make_corner_list(data)
    print(corner_list)
    total = area_from_corners(corner_list, data)
    return total


def task2(data):
    total = 0
    corner_list = make_corner_list(data)
    print(corner_list)
    total = area_from_corners(corner_list, data)
    return total


def main():
    data = load_data()
    print_matrix(data)
    print(f'Task 1: {task1(copy.deepcopy(data))}')

    real_data = extract_from_hex(data)
    print(f'Task 2: {task2(copy.deepcopy(real_data))}')


if __name__ == '__main__':
    main()
