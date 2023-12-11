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

    expanded_galaxy_in_x = []
    for i in range(len(expanded_galaxy_in_y)):
        expanded_galaxy_in_x.append([])

    for col_index in range(len(expanded_galaxy_in_y[0])):
        col = [row[col_index] for row in expanded_galaxy_in_y]
        for row_index in range(len(col)):
            expanded_galaxy_in_x[row_index].append(col[row_index])
            if '#' not in col:
                expanded_galaxy_in_x[row_index].append(col[row_index])
    return expanded_galaxy_in_x


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


def task1(data):
    expanded_galaxy = expand_galaxy(data)
    galaxies = find_galaxies(expanded_galaxy)
    distances = get_distances(galaxies)
    return sum(distances)


def task2(data):
    return None


def main():
    data = load_data()

    print(f'Task 1: {task1(data)}')
    print(f'Task 2: {task2(data)}')


if __name__ == '__main__':
    main()
