class Number:
    def __init__(self, val, start_x, end_x, y):
        self.val = val
        self.start_x = start_x
        self.end_x = end_x
        self.y = y

    def __str__(self):
        return f'Number(val={self.val}, start_x={self.start_x}, end_x={self.end_x}, y={self.y})'


class Gear:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Gear(x={self.x}, y={self.y})'


def load_data():
    with open('schematic') as f:
        data = []
        for line in f.readlines():
            data.append(line)
        return data


def extract_numbers_in_line(line):
    numbers = []
    pos = 0
    current_number = ''
    current_start = 0
    current_end = 0
    for char in line:
        if char.isdigit():
            # first digit of number
            if current_number == '':
                current_start = pos
                current_number += char
            # next digit of number
            else:
                current_number += char
        else:
            # not a digit and not in number
            if current_number == '':
                pass
            # leaving current number
            else:
                current_end = pos-1
                numbers.append(Number(int(current_number), current_start, current_end, 0))
                current_number = ''
        pos += 1
    return numbers


def extract_all_numbers(data):
    numbers = []
    line_no = 0
    for line in data:
        numbers_in_line = extract_numbers_in_line(line)
        for number in numbers_in_line:
            number.y = line_no
            numbers.append(number)
        line_no += 1
    return numbers


def get_only_part_numbers(numbers, data, special_characters):
    part_numbers = []
    for number in numbers:
        if number.y-1 < 0:
            start_y = 0
        else:
            start_y = number.y-1

        if number.y+1 > len(data)-1:
            end_y = len(data)-1
        else:
            end_y = number.y+1

        if number.start_x-1 < 0:
            start_x = 0
        else:
            start_x = number.start_x-1

        if number.end_x+1 > len(data[0])-1:
            end_x = len(data[0])-1
        else:
            end_x = number.end_x+1

        is_part_number = False
        for line in data[start_y:end_y+1]:
            for char in line[start_x:end_x+1]:
                if char in special_characters:
                    is_part_number = True
                    break

        if is_part_number:
            part_numbers.append(number)

    return part_numbers


def get_potential_gear_positions(data):
    potential_gear_positions = []
    y = 0
    for line in data:
        x = 0
        for char in line:
            if char == '*':
                potential_gear_positions.append(Gear(x, y))
            x += 1
        y += 1
    return potential_gear_positions


def get_gear_ratios(potential_gear_positions, potential_gear_numbers):
    gear_ratios = []
    for gear_position in potential_gear_positions:
        adjacent_numbers = []
        for gear_number in potential_gear_numbers:
            if gear_number.y in range(gear_position.y-1, gear_position.y+2):
                if gear_position.x in range(gear_number.start_x-1, gear_number.end_x+2):
                    adjacent_numbers.append(gear_number)
        if len(adjacent_numbers) == 2:
            gear_ratios.append(adjacent_numbers)
    return gear_ratios


def main():
    data = load_data()
    print(data)

    numbers = extract_all_numbers(data)

    for number in numbers:
        print(number)

    data_no_lend = []
    for line in data:
        line = line.replace('\n', '')
        data_no_lend.append(line)

    # Task 1

    part_numbers = get_only_part_numbers(numbers, data_no_lend, '!@#$%^&*()-+?_=,<>/')

    total = 0
    for number in part_numbers:
        total += number.val

    print(f'Task 1: {total}')

    # Task 2

    potential_gear_numbers = get_only_part_numbers(numbers, data_no_lend, '*')
    potential_gear_positions = get_potential_gear_positions(data_no_lend)
    gear_ratios = get_gear_ratios(potential_gear_positions, potential_gear_numbers)

    print(f'Potential gear numbers:')
    for number in potential_gear_numbers:
        print(number)
    print(f'Potential gear positions:')
    for position in potential_gear_positions:
        print(position)

    print(f'Gear ratios:')
    total = 0
    for pair in gear_ratios:
        total += pair[0].val * pair[1].val
    print(f'Task 2: {total}')


if __name__ == '__main__':
    main()
