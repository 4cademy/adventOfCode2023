def load_data():
    data = []
    with open('races') as f:
        for line in f.readlines():
            line = line.strip()
            line = line.split(':')
            line = line[1].split(' ')
            line = [x for x in line if x != '']
            line = [int(x) for x in line]
            data.append(line)
    return data


def load_data2():
    data = load_data()
    data2 = ['', '']
    for i in range(len(data[0])):
        data2[0] += f'{data[0][i]}'
        data2[1] += f'{data[1][i]}'

    data2[0] = int(data2[0])
    data2[1] = int(data2[1])
    return data2


def get_winning_possibilities(time, best_distance):
    winning_possibilities = []
    for i in range(time):
        speed = i
        remaining_time = time - i
        distance = speed * remaining_time
        if distance > best_distance:
            winning_possibilities.append(i)
    return winning_possibilities


def get_winning_count(time, best_distance):
    winning_possibilities = get_winning_possibilities(time, best_distance)
    return len(winning_possibilities)


def main():
    data = load_data()
    total = 1
    for race_index in range(len(data[0])):
        total *= get_winning_count(data[0][race_index], data[1][race_index])
    print(f'Task 1: {total}')

    data = load_data2()
    print(f'Task 2: {get_winning_count(load_data2()[0], load_data2()[1])}')


if __name__ == '__main__':
    main()
