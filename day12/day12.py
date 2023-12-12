import copy

def load_data():
    data = []
    with open('springs_test1') as f:
        for line in f.readlines():
            line = line.strip()
            data.append(line)
    return data


def reformat_data(data):
    refomated_data = []
    for line in data:
        line = line.split(' ')
        line[1] = line[1].split(',')
        line[1] =[int(x) for x in line[1]]
        refomated_data.append(line)
    return refomated_data


def find_first_fit(string, length):
    for i in range(len(string)):
        if i+length > len(string):
            return -1
        if '.' not in string[i:i+length]:
            return i


def find_all_fits(string, length):
    all_fits = []
    last_index = 0
    index = find_first_fit(string, length)
    while index != -1 and len(string) >= length:
        all_fits.append(last_index + index)
        string = string[index+1:]
        last_index += index + 1
        index = find_first_fit(string, length)
    return all_fits


def find_fits_for_multiple_segments(string, lengths):
    if len(lengths) == 1:
        list_of_fits = []
        fits = find_all_fits(string, lengths[0])
        for fit in fits:
            list_of_fits.append([fit, fit + lengths[0] - 1])
        return list_of_fits
    else:
        length = lengths.pop(0)
        working_string = string[length:]
        list_of_fits = find_fits_for_multiple_segments(working_string, lengths)
        new_list_of_fits = []
        for fit in list_of_fits:
            new_list_of_fits.append([fit[0] + length, fit[1] + length])


def task1(data):
    total = 0
    all_fits = rekursive_find_all_fits('.???.?##', [1])
    print(all_fits)
    return total


def task2(data):
    return


def main():
    data = load_data()
    data = reformat_data(data)

    for line in data:
        print(line)

    print(f'Task 1: {task1(data)}')
    print(f'Task 2: {task2(data)}')


if __name__ == '__main__':
    main()
