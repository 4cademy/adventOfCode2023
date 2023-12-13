def load_data():
    data = []
    section = []
    with open('mirrors') as f:
        for line in f.readlines():
            line = line.strip()
            if line == '':
                data.append(section)
                section = []
            else:
                section.append(line)
        data.append(section)
    return data


def mirror_here_in_line(line, pos):
    is_mirror = True
    for i in range(1, min(pos, len(line) - pos)+1, 1):
        char_left = line[pos - i]
        char_right = line[pos + i - 1]
        if char_left != char_right:
            is_mirror = False
            break
    return is_mirror


def vertical_mirror_here(sequence, pos):
    is_mirror = True
    for line in sequence:
        if not mirror_here_in_line(line, pos):
            is_mirror = False
            break
    return is_mirror


def find_vertical_mirror(sequence):
    for i in range(1, len(sequence[0]), 1):
        if vertical_mirror_here(sequence, i):
            return i
    return None


def horizontal_mirror_here(sequence, pos):
    is_mirror = True
    for i in range(1, min(pos, len(sequence) - pos)+1, 1):
        line_above = sequence[pos - i]
        line_below = sequence[pos + i - 1]
        if line_above != line_below:
            is_mirror = False
            break
    return is_mirror


def find_horizontal_mirror(sequence):
    for i in range(1, len(sequence), 1):
        if horizontal_mirror_here(sequence, i):
            return i
    return None


# for task 2
def mirror_here_in_line_with_num_of_differences(line, pos):
    smudge_count = 0
    for i in range(1, min(pos, len(line) - pos)+1, 1):
        char_left = line[pos - i]
        char_right = line[pos + i - 1]
        if char_left != char_right:
            smudge_count += 1
    return smudge_count


def vertical_mirror_here_with_num_of_differences(sequence, pos):
    smudge_count = 0
    for line in sequence:
        smudge_count += mirror_here_in_line_with_num_of_differences(line, pos)
    return smudge_count


def find_vertical_mirror_with_num_of_differences(sequence):
    for i in range(1, len(sequence[0]), 1):
        if vertical_mirror_here_with_num_of_differences(sequence, i) == 1:
            return i
    return None


def count_differences(string1, string2):
    return sum(c1 != c2 for c1, c2 in zip(string1, string2))


def horizontal_mirror_here_with_num_of_differences(sequence, pos):
    smudge_count = 0
    for i in range(1, min(pos, len(sequence) - pos)+1, 1):
        line_above = sequence[pos - i]
        line_below = sequence[pos + i - 1]
        if line_above != line_below:
            smudge_count += count_differences(line_above, line_below)
    return smudge_count


def find_horizontal_mirror_with_num_of_differences(sequence):
    for i in range(1, len(sequence), 1):
        if horizontal_mirror_here_with_num_of_differences(sequence, i) == 1:
            return i
    return None


def task1(data):
    total = 0
    for section in data:
        mirror_pos = find_vertical_mirror(section)
        result = mirror_pos
        if mirror_pos is None:
            mirror_pos = find_horizontal_mirror(section)
            result = mirror_pos * 100
        total += result
    return total


def task2(data):
    total = 0
    for section in data:
        mirror_pos = find_vertical_mirror_with_num_of_differences(section)
        result = mirror_pos
        if mirror_pos is None:
            mirror_pos = find_horizontal_mirror_with_num_of_differences(section)
            result = mirror_pos * 100
        total += result
    return total


def main():
    data = load_data()
    for section in data:
        for line in section:
            print(line)
        print()

    print(f'Task 1: {task1(data)}')
    print(f'Task 2: {task2(data)}')


if __name__ == '__main__':
    main()