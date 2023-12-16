import copy


def load_data():
    data = []
    with open('hashs_test1') as f:
        line = f.readline().strip()
        data = line.split(',')
    return data


def task1(data):
    total = 0
    return total


def task2(data):
    total = 0
    return total


def main():
    data = load_data()
    print(data)

    print(f'Task 1: {task1(copy.deepcopy(data))}')
    print(f'Task 2: {task2(copy.deepcopy(data))}')


if __name__ == '__main__':
    main()
