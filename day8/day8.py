def load_data():
    data = []
    with open('map') as f:
        for line in f.readlines():
            line = line.strip()
            data.append(line)
    return data


def get_sequence(data):
    return data[0]


def get_paths(data):
    paths = []
    for line in data[2:]:
        line = line.replace('(', '')
        line = line.replace(')', '')
        line = line.replace(',', '')
        line = line.replace('=', '')
        line = line.replace(' ', '')
        paths.append([line[0:3], line[3:6], line[6:9]])

    return paths


def get_path_index(paths, start):
    for p in paths:
        if p[0] == start:
            return paths.index(p)


def get_starts(paths):
    starts = []
    for p in paths:
        start = p[0]
        if start[2] == 'A':
            starts.append(start)
    return starts


def get_ends(paths):
    ends = []
    for p in paths:
        end = p[0]
        if end[2] == 'Z':
            ends.append(end)
    return ends


def get_no_of_steps(sequence, paths):
    sequence_index = 0
    start = 'VKA'
    while True:
        count = 0
        do_anyway = True
        while do_anyway or start[2] != 'Z':
            do_anyway = False
            path_index = get_path_index(paths, start)
            path = paths[path_index]
            next_to_check = sequence[sequence_index]
            if next_to_check == 'L':
                start = path[1]
            else:
                start = path[2]

            sequence_index += 1
            if sequence_index == len(sequence):
                sequence_index = 0

            count += 1
        print(count, start)
    return count


def all_are_ends(starts, ends):
    check = True
    for start in starts:
        if start not in ends:
            check = False
    return check


def get_no_of_steps2(sequence, paths):
    count = 0
    sequence_index = 0
    starts = get_starts(paths)
    ends = get_ends(paths)
    print(starts)
    print(ends)
    while not all_are_ends(starts, ends):
        next_to_check = sequence[sequence_index]

        for i in range(len(starts)):
            path_index = get_path_index(paths, starts[i])
            path = paths[path_index]

            if next_to_check == 'L':
                starts[i] = path[1]
            else:
                starts[i] = path[2]

        sequence_index += 1
        if sequence_index == len(sequence):
            sequence_index = 0
        count += 1
        # print(count, starts)
    return count


def main():
    data = load_data()
    paths = get_paths(data)
    sequence = get_sequence(data)
    starts = get_starts(paths)
    ends = get_ends(paths)

    no_of_steps = get_no_of_steps(sequence, paths)
    print(no_of_steps)


if __name__ == '__main__':
    main()
