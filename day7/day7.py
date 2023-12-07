def load_data():
    data = []
    with open('hands') as f:
        for line in f.readlines():
            line = line.strip()
            line = line.split(' ')
            line[1] = int(line[1])
            data.append(line)
    return data


def get_hand_type(hand):
    if 'J' in hand:
        most_card_number = 0
        most_card = None
        if hand.count('J') == 5:
            return 6
        else:
            for card in set(hand) - {'J'}:
                if hand.count(card) > most_card_number:
                    most_card_number = hand.count(card)
                    most_card = card
            hand = hand.replace('J', str(most_card))

    hand_type = None
    if len(set(hand)) == 1:     # all cards are the same
        hand_type = 6
    elif len(set(hand)) == 2:    # four of a kind or full house
        hand_type = 4   # set full house as default
        for card in set(hand):
            if hand.count(card) == 4:   # four of a kind
                hand_type = 5
    elif len(set(hand)) == 3:    # three of a kind or two pairs
        hand_type = 2   # set two pairs as default
        for card in set(hand):
            if hand.count(card) == 3:  # three of a kind
                hand_type = 3
    elif len(set(hand)) == 4:
        hand_type = 1
    else:
        hand_type = 0
    return hand_type


def get_card_value(card):
    if card == '2':
        return 2
    elif card == '3':
        return 3
    elif card == '4':
        return 4
    elif card == '5':
        return 5
    elif card == '6':
        return 6
    elif card == '7':
        return 7
    elif card == '8':
        return 8
    elif card == '9':
        return 9
    elif card == 'T':
        return 10
    elif card == 'J':
        return 1
    elif card == 'Q':
        return 12
    elif card == 'K':
        return 13
    elif card == 'A':
        return 14
    else:
        return None


def need_to_swap(hand1, hand2):
    hand1_type = get_hand_type(hand1)
    hand2_type = get_hand_type(hand2)
    if hand1_type < hand2_type:
        return True
    elif hand1_type > hand2_type:
        return False
    else:
        for i in range(len(hand1)):
            if get_card_value(hand1[i]) > get_card_value(hand2[i]):
                return False
            elif get_card_value(hand1[i]) < get_card_value(hand2[i]):
                return True
    return False


def sort_data(data):
    changed = True
    while changed:
        changed = False
        for i in range(len(data)-1):
            if need_to_swap(data[i][0], data[i+1][0]):
                data[i], data[i+1] = data[i+1], data[i]
                changed = True
    return data


def main():
    data = load_data()
    data = sort_data(data)
    total = 0
    for i in range(len(data)):
        print(data[i])
        total += data[i][1] * (len(data) - i)
    print(total)


if __name__ == '__main__':
    main()
