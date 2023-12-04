def load_data():
    with open('cards') as f:
        data = []
        for line in f.readlines():
            card = line.strip()
            card = card.split(':')
            card = card[1]
            card = card.split('|')

            index = 0
            for number_sektion in card:
                number_sektion = number_sektion.split(' ')
                number_sektion = [x for x in number_sektion if x != '']
                number_sektion = [int(x) for x in number_sektion]

                card[index] = number_sektion
                index += 1

            data.append(card)

        return data


def get_winning_numbers(card):
    winning_numbers = []
    for number in card[1]:
        if number in card[0]:
            winning_numbers.append(number)
    return winning_numbers


def amount_of_each_card(cards):
    amount_array = [1 for i in range(0, len(cards))]

    card_index = 0
    for card in cards:
        no_winning_numbers = len(get_winning_numbers(card))
        if no_winning_numbers > 0:
            for i in range(0, no_winning_numbers):
                amount_array[card_index+1+i] += amount_array[card_index]
        card_index += 1

    return amount_array[0:len(cards)]


if __name__ == '__main__':
    cards = load_data()

    total = 0

    amounts = amount_of_each_card(cards)

    print(sum(amounts))
