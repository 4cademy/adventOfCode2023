import copy


class Element:
    label: str
    label_hash: int
    sign: str
    num: int

    def __str__(self):
        return f'{self.label} ({self.label_hash}) {self.sign} {self.num}'


def load_data():
    data = []
    with open('hashs') as f:
        line = f.readline().strip()
        data = line.split(',')
    return data


def load_data2(data):
    data = load_data()
    data2 = []
    for elem in data:
        for i, char in enumerate(elem):
            if char == '=' or char == '-':
                e = Element()
                e.label = elem[:i]
                e.label_hash = hash_algo(e.label)
                e.sign = char
                if i+1 < len(elem):
                    e.num = int(elem[i+1:])
                else:
                    e.num = None
                data2.append(e)
                break
    return data2


def hash_algo(string):
    total = 0
    for char in string:
        total += ord(char)
        total *= 17
        total %= 256
    return total


def create_map(length):
    my_map = []
    for i in range(length):
        my_map.append([])
    return my_map


def label_in_box(box, lens):
    for i, elem in enumerate(box):
        if elem.label == lens.label:
            return i
    return -1


def change_map(my_map, elem):
    box = my_map[elem.label_hash]
    if elem.sign == '=':
        if len(box) == 0:
            box.append(elem)
        else:
            if label_in_box(box, elem) == -1:
                box.append(elem)
            else:
                box[label_in_box(box, elem)].num = elem.num
    elif elem.sign == '-':
        if len(box) == 0:
            pass
        else:
            if label_in_box(box, elem) != -1:
                box.pop(label_in_box(box, elem))


def task1(data):
    total = 0
    for string in data:
        print(f'{string} -> {hash_algo(string)}')
        total += hash_algo(string)
    return total


def task2(data):
    total = 0
    hashmap = create_map(256)
    for elem in data:
        change_map(hashmap, elem)
    for i, box in enumerate(hashmap):
        for j, lens in enumerate(box):
            total += (i+1)*(j+1)*lens.num
    return total


def main():
    data = load_data()
    print(data)
    print(f'Task 1: {task1(copy.deepcopy(data))}')

    data2 = load_data2(data)
    for elem in data2:
        print(elem)
    print(f'Task 2: {task2(copy.deepcopy(data2))}')


if __name__ == '__main__':
    main()
