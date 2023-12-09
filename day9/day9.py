def load_data():
    data = []
    with open('oasis') as f:
        for line in f.readlines():
            line = line.strip()
            line = line.split(' ')
            line = [int(x) for x in line]
            data.append(line)
    return data


def get_next_sequence(sequence):
    next_sequence = []
    for i in range(len(sequence) - 1):
        next_sequence.append(sequence[i + 1] - sequence[i])
    return next_sequence


def seq_only_zeros(sequence):
    for i in sequence:
        if i != 0:
            return False
    return True


def reduce_seq_to_zero(sequence):
    sequences = [sequence]
    while not seq_only_zeros(sequence):
        sequence = get_next_sequence(sequence)
        sequences.append(sequence)
    return sequences


def roll_back_reduction_last(sequences):
    next_num = 0
    no_of_steps = len(sequences)
    for i in range(no_of_steps-1, -1, -1):
        next_num += sequences[i][-1]
    return next_num


def roll_back_reduction_first(sequences):
    next_num = 0
    no_of_steps = len(sequences)
    for i in range(no_of_steps-1, -1, -1):
        next_num = sequences[i][0]-next_num
    return next_num


def task1(data):
    total = 0
    for seq in data:
        reduction = reduce_seq_to_zero(seq)
        total += roll_back_reduction_last(reduction)
    return total


def task2(data):
    total = 0
    for seq in data:
        reduction = reduce_seq_to_zero(seq)
        total += roll_back_reduction_first(reduction)
    return total


def main():
    data = load_data()
    print(f'Task 1: {task1(data)}')
    print(f'Task 2: {task2(data)}')


if __name__ == '__main__':
    main()
