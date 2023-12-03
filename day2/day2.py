r_max = 12
g_max = 13
b_max = 14

def load_data():
    with open('game_doc') as f:
        data = []
        for line in f.readlines():
            data.append(line.strip())

        data2 = []
        for game in data:
            game = game.replace(' ', '')
            game = game.split(':')
            game = game[1].split(';')
            index = 0
            for hand in game:
                hand = hand.split(',')
                game[index] = hand
                index += 1
            data2.append(game)

        return data2


def valid_color(color):
    if 'red' in color:
        color = color.replace('red', '')
        if int(color) > r_max:
            return False
    elif 'green' in color:
        color = color.replace('green', '')
        if int(color) > g_max:
            return False
    elif 'blue' in color:
        color = color.replace('blue', '')
        if int(color) > b_max:
            return False
    return True


def valid_hand(hand):
    for color in hand:
        if not valid_color(color):
            return False
    return True


def valid_game(game):
    for hand in game:
        if not valid_hand(hand):
            return False
    return True


def get_red(hand):
    for color in hand:
        if 'red' in color:
            number = color.replace('red', '')
            return int(number)
    return 0


def get_green(hand):
    for color in hand:
        if 'green' in color:
            number = color.replace('green', '')
            return int(number)
    return 0


def get_blue(hand):
    for color in hand:
        if 'blue' in color:
            number = color.replace('blue', '')
            return int(number)
    return 0


def max_red(game):
    max_val = 0
    for hand in game:
        red_in_hand = get_red(hand)
        if red_in_hand > max_val:
            max_val = red_in_hand
    return max_val


def max_green(game):
    max_val = 0
    for hand in game:
        green_in_hand = get_green(hand)
        if green_in_hand > max_val:
            max_val = green_in_hand
    return max_val


def max_blue(game):
    max_val = 0
    for hand in game:
        blue_in_hand = get_blue(hand)
        if blue_in_hand > max_val:
            max_val = blue_in_hand
    return max_val


def main():
    data = load_data()
    print(data)

    game_no = 1
    total1 = 0
    for game in data:
        if valid_game(game):
            total1 += game_no
        game_no += 1
    print(f'Task 1: {total1}')

    total2 = 0
    for game in data:
        total2 += max_red(game) * max_green(game) * max_blue(game)
    print(f'Task 2: {total2}')


if __name__ == '__main__':
    main()
