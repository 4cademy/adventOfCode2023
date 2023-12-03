def load_data():
    with open('calibration_doc') as f:
        data = []
        for line in f.readlines():
            data.append(line.strip())
        return data


def extract_first_digit(line):
    for char in line:
        if char.isdigit():
            return char


def extract_last_digit(line):
    for char in reversed(line):
        if char.isdigit():
            return char


def replace_word_with_digit(line):
    # replace special cases
    line = line.replace('twone', 'twoone')
    line = line.replace('eightwo', 'eighttwo')
    line = line.replace('eighthree', 'eightthree')
    line = line.replace('oneight', 'oneeight')
    line = line.replace('threeight', 'threeeight')
    line = line.replace('fiveight', 'fiveeight')
    line = line.replace('nineight', 'nineeight')

    line = line.replace('one', '1')
    line = line.replace('two', '2')
    line = line.replace('three', '3')
    line = line.replace('four', '4')
    line = line.replace('five', '5')
    line = line.replace('six', '6')
    line = line.replace('seven', '7')
    line = line.replace('eight', '8')
    line = line.replace('nine', '9')
    return line


def refactor_array(array):
    refactored_array = []
    for line in array:
        line = replace_word_with_digit(line)
        refactored_array.append(line)
    return refactored_array


def extract_all_digit_numbers(array):
    numbers = []
    for line in array:
        numbers.append(extract_first_digit(line) + extract_last_digit(line))
    return numbers


def main():
    data = load_data()

    data = refactor_array(data)

    print(data)

    all_numbers = extract_all_digit_numbers(data)

    print(all_numbers)

    total = 0
    for number in all_numbers:
        total += int(number)

    print(f'Total: {total}')


if __name__ == '__main__':
    main()
