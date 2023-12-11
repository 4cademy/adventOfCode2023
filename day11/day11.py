def load_data():
    data = []
    with open('galaxy') as f:
        for line in f.readlines():
            line = line.strip()
            data.append(line)
    return data


def expand_galaxy(data):
    expanded_galaxy_in_y = []
    for line in data:
        expanded_galaxy_in_y.append(line)
        if '#' not in line:
            expanded_galaxy_in_y.append(line)

    inverted_galaxy = []
    for i in range(len(expanded_galaxy_in_y[0])):
        inverted_galaxy.append('')
    for line in expanded_galaxy_in_y:
        for i in range(len(line)):
            inverted_galaxy[i] += line[i]

    expanded_galaxy_in_x = []
    for line in inverted_galaxy:
        expanded_galaxy_in_x.append(line)
        if '#' not in line:
            expanded_galaxy_in_x.append(line)

    return expanded_galaxy_in_x


def get_coords_to_expand(data):
    rows_to_expand = []
    cols_to_expand = []
    for y in range(len(data)):
        if '#' not in data[y]:
            rows_to_expand.append(y)

    for x in range(len(data[0])):
        if '#' not in [line[x] for line in data]:
            cols_to_expand.append(x)
    return rows_to_expand, cols_to_expand


def find_galaxies(data):
    galaxies = []
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == '#':
                galaxies.append((x, y))
    return galaxies


def get_distances(galaxies):
    distances = []
    while galaxies:
        galaxy = galaxies.pop()
        for other_galaxy in galaxies:
            distance = abs(galaxy[0] - other_galaxy[0]) + abs(galaxy[1] - other_galaxy[1])
            distances.append(distance)
    return distances


def get_distances_with_expansion_data(galaxies, rows_to_expand, cols_to_expand):
    expansion = 999999
    distances = []
    while galaxies:
        galaxy = galaxies.pop()
        for other_galaxy in galaxies:
            distance = abs(galaxy[0] - other_galaxy[0]) + abs(galaxy[1] - other_galaxy[1])
            for row in rows_to_expand:
                if galaxy[1] < row < other_galaxy[1]:
                    distance += expansion
                elif other_galaxy[1] < row < galaxy[1]:
                    distance += expansion
            for col in cols_to_expand:
                if galaxy[0] < col < other_galaxy[0]:
                    distance += expansion
                elif other_galaxy[0] < col < galaxy[0]:
                    distance += expansion
            distances.append(distance)
    return distances


def task1(data):
    expanded_galaxy = expand_galaxy(data)
    galaxies = find_galaxies(expanded_galaxy)
    distances = get_distances(galaxies)
    return sum(distances)


def task2(data):
    rows_to_expand, cols_to_expand = get_coords_to_expand(data)
    distances = get_distances_with_expansion_data(find_galaxies(data), rows_to_expand, cols_to_expand)
    return sum(distances)


def main():
    data = load_data()

    print(f'Task 1: {task1(data)}')
    print(f'Task 2: {task2(data)}')


if __name__ == '__main__':
    main()
