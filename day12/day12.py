import copy
import threading


thread_no = 8
thread_sums = [0 for i in range(thread_no)]


def load_data():
    data = []
    with open('springs') as f:
        for line in f.readlines():
            line = line.strip()
            data.append(line)
    return data


def reformat_data(data):
    reformatted_data = []
    for line in data:
        line = line.split(' ')
        line[1] = line[1].split(',')
        line[1] = [int(x) for x in line[1]]
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
    for i in range(len(string) - length + 1):
        if '.' not in string[i:i + length]:
            fits.append([i, i + length - 1])
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
                    if fit[-1][1] < next_fit[0] - 1:
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
            for i in range(segment[0], segment[1] + 1):
                tmp = tmp[:i] + 'M' + tmp[i + 1:]
        # print(f'Fit: {tmp}')
        if '#' not in tmp:
            actual_fits.append(fit)

    return actual_fits


# functions for task 2


def find_fits_of_first_element(string, lengths, offset=0):
    fits = []
    l = lengths[0]
    a = len(string)
    b = sum(lengths)
    c = len(lengths)
    search_width = len(string) - (sum(lengths) + len(lengths) - 1)
    if search_width < 0:
        return fits
    for i in range(search_width + 1):
        if '.' not in string[i:i + l]:
            if i + l < len(string):
                if '#' != string[i + l]:
                    remaining_string = string[i + l:]
                    fits.append((offset + i, offset + i + lengths[0] - 1, remaining_string))
            elif i-1 >= 0:
                if '#' != string[i - 1]:
                    remaining_string = string[i + l:]
                    fits.append((offset + i, offset + i + lengths[0] - 1, remaining_string))
            else:
                fits.append((offset + i, offset + i + lengths[0] - 1, ''))
    return fits


def find_all_fits(string, lengths, offset=0):
    fits = []
    if len(lengths) == 1:
        fits = []
        fits_and_remaining_string = find_fits_of_first_element(string, lengths, offset=offset)
        for fit in fits_and_remaining_string:
            fits.append([[fit[0], fit[1]]])
    else:
        fits_and_remaining_string = find_fits_of_first_element(string, lengths, offset=offset)
        remaining_lengths = lengths[1:]
        for fit in fits_and_remaining_string:
            remaining_string = fit[2][1:]
            remaining_fits = find_all_fits(remaining_string, remaining_lengths, offset=fit[1] + 2)
            for rf in remaining_fits:
                new_fit = [[fit[0], fit[1]]] + rf
                fits.append(new_fit)
    return fits



def find_all_fits2(string, lengths, offset=0):
    if len(lengths) == 1:
        fits_and_remaining_string = find_fits_of_first_element(string, lengths, offset=offset)
        for fit in fits_and_remaining_string:
            yield [[fit[0], fit[1]]]
    else:
        fits_and_remaining_string = find_fits_of_first_element(string, lengths, offset=offset)
        remaining_lengths = lengths[1:]
        for fit in fits_and_remaining_string:
            remaining_string = fit[2][1:]
            remaining_fits = find_all_fits2(remaining_string, remaining_lengths, offset=fit[1] + 2)
            for rf in remaining_fits:
                new_fit = [[fit[0], fit[1]]] + rf
                yield new_fit


def filter_actual_fits(string, fits):
    actual_fits = []
    for fit in fits:
        # print(f'Checking fit {fit}')
        tmp = string
        for segment in fit:
            for i in range(segment[0], segment[1] + 1):
                tmp = tmp[:i] + 'M' + tmp[i + 1:]
        # print(f'Fit: {tmp}')
        if '#' not in tmp:
            actual_fits.append(fit)
    return actual_fits


def task1(data):
    total = 0
    for line in data:
        all_fits = find_fits_for_multiple_segments(line[0], line[1])
        total += len(all_fits)
    return total


def task2(data):
    total = 0
    for line in data:
        all_fits = find_all_fits(line[0], line[1])
        actual_fits = filter_actual_fits(line[0], all_fits)
        total += len(actual_fits)
        print(f'Found {len(actual_fits)} fits for {line[0]}')
    return total


def task2_2(data, start=0):
    total = 0
    for line in data:
        all_fits = find_all_fits2(line[0], line[1])
        actual_fits = filter_actual_fits(line[0], all_fits)
        total += len(list(actual_fits))
        line_index = data.index(line) + start
        print(f'{line_index}: {len(list(actual_fits))}')
    return total


def multithreading_task2(data):
    thread_list = []
    global thread_no
    for i in range(thread_no):
        thread_list.append(threading.Thread(target=task2_2, args=(
            data[i * len(data) // thread_no:(i + 1) * len(data) // thread_no], i * len(data) // thread_no)))

    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        thread.join()

    return 'Finished'


def check_next(string, lengths, must_check_next=False):
    # match
    if '#' not in string and len(lengths) == 1 and lengths[0] == 0:
        return 1
    # no match
    elif not string or not lengths:
        return 0
    # further check
    else:
        char = string[0]
        string = string[1:]
        if must_check_next:
            if lengths[0] == 0:
                if char == '#':
                    return 0
                return check_next(string, lengths.copy()[1:], False)
            else:
                if char == '.':
                    return 0
                else:
                    lengths[0] -= 1
                    return check_next(string, lengths.copy(), True)
        else:
            if char == '.':
                return check_next(string, lengths.copy())
            elif char == '#':
                lengths[0] -= 1
                return check_next(string, lengths.copy(), True)
            elif char == '?':
                return check_next('.' + string, lengths.copy()) + check_next('#' + string, lengths.copy())


def main():
    data = load_data()
    data = reformat_data(data)

    # print(f'Task 1: {task1(data)}')

    data = expand_data()
    # print(f'Task 2: {task2_2(data)}')

    total = 0
    for line in data:
        res = check_next(line[0], line[1])
        print(f'line {data.index(line)}: {res}')
        total += check_next(line[0], line[1])
    print('------------------')
    print(f'Task 2: {total}')


if __name__ == '__main__':
    main()
