import copy


def load_data():
    data = []
    with open('springs_test1') as f:
        for line in f.readlines():
            line = line.strip()
            data.append(line)
    return data


def reformat_data(data):
    reformatted_data = []
    for line in data:
        line = line.split(' ')
        line[1] = line[1].split(',')
        line[1] =[int(x) for x in line[1]]
        reformatted_data.append(line)
    return reformatted_data


def expand_data():
    data = load_data()
    reformatted_data = reformat_data(data)
    expanded_data = []
    for line in reformatted_data:
        line[0] = line[0] + '?' + line[0] + '?' + line[0] + '?' + line[0] + '?' + line[0]
        line[1] = line[1] + line[1] + line[1] + line[1] + line[1]
        expanded_data.append(line)
    return expanded_data


def find_fits_in_string(string, length):
    fits = []
    for i in range(len(string)-length+1):
        if '.' not in string[i:i+length]:
            fits.append([i, i+length-1])
    return fits


def find_fits_for_multiple_segments(string, lengths):
    # print(f'Finding fits for {string} with lengths {lengths}')
    fits = []
    for length in lengths:
        print(f'Finding fits for length {length}')
        fits_for_this_length = find_fits_in_string(string, length)
        if fits:
            new_fits = []
            for fit in fits:
                for next_fit in fits_for_this_length:
                    if fit[-1][1] < next_fit[0]-1:
                        new_fits.append(fit + [next_fit])
            fits = copy.deepcopy(new_fits)
        else:
            for fit in fits_for_this_length:
                fits.append([fit])

    actual_fits = []
    for fit in fits:
        # print(f'Checking fit {fit}')
        tmp = string
        for segment in fit:
            for i in range(segment[0], segment[1]+1):
                tmp = tmp[:i] + 'M' + tmp[i+1:]
        # print(f'Fit: {tmp}')
        if '#' not in tmp:
            actual_fits.append(fit)

    return actual_fits

# functions for task 2


def find_fits_of_first_element(string, lengths):
    fits = []
    l = lengths[0]
    a = len(string)
    b = sum(lengths)
    c = len(lengths)
    search_width = len(string)-(sum(lengths)+len(lengths)-1)
    if search_width < 0:
        return fits
    for i in range(search_width+1):
        if '.' not in string[i:i+l] and '#' != string[i+l]:
            remaining_string = string[i+l:]
            fits.append((i, i+lengths[0]-1, remaining_string))
    return fits


def find_all_fits(string, lengths):
    fits = []
    if len(lengths) == 1:
        fits = []
        fits_and_remaining_string = find_fits_of_first_element(string, lengths)
        for fit in fits_and_remaining_string:
            fits.append((fit[0], fit[1], ''))
    else:
        fits_and_remaining_string = find_fits_of_first_element(string, lengths)
        for fit in fits_and_remaining_string:
            remaining_string = fit[2]
            remaining_lengths = lengths[1:]
            remaining_fits = find_all_fits(remaining_string, remaining_lengths)
            for rm in remaining_fits:
                fits.append(fit)
                fits.append(rm)
    return fits


def task1(data):
    total = 0
    for line in data:
        all_fits = find_fits_for_multiple_segments(line[0], line[1])
        total += len(all_fits)
    return total


def task2(data):
    total = 0
    print(data[1])
    print('------------------')
    all_fits = find_all_fits(data[1][0], data[1][1])
    for elem in all_fits:
        print(elem)
    return total


def main():
    data = load_data()
    data = reformat_data(data)

    # print(f'Task 1: {task1(data)}')

    data = expand_data()
    print(f'Task 2: {task2(data)}')


if __name__ == '__main__':
    main()
