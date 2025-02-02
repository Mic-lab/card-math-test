from random import shuffle

fg = lambda text, color: "\33[38;5;" + str(color) + "m" + text + "\33[0m"
bg = lambda text, color: "\33[48;5;" + str(color) + "m" + text + "\33[0m"

class Card:

    SUIT_STYLE = {
        'spades': {
            'color': 0,
            'symbol': '♤',
        },
        'clubs': {
            'color': 18,
            'symbol': '♧',
        },
        'diamonds': {
            'color': 94,
            'symbol': '♢',
        },
        'hearts': {
            'color': 88,
            'symbol': '♡',
        },

    }

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    @property
    def style(self):
        return Card.SUIT_STYLE[self.suit]

    @property
    def value(self):
        if self.rank == 'A':
            return 11
        elif self.rank in set('KQJ'):
            return 10
        else:
            return int(self.rank)

    def __len__(self):
        return len(self.base_str())

    def base_str(self):
        return f'{self.value} {self.style["symbol"]}'

    def __str__(self):
        return bg(self.base_str(), self.style['color'])

class Deck:
    def __init__(self):
        self.cards = self.get_cards()

    def get_cards(self):

        deck = []

        for suit in {'spades', 'clubs', 'hearts', 'diamonds'}:
            for i in range(1, 14):
                if i == 1:
                    rank = 'A'
                elif i == 11:
                    rank = 'J'
                elif i == 12:
                    rank = 'Q'
                elif i == 13:
                    rank = 'K'
                else:
                    rank = str(i)

                deck.append(Card(suit, rank))

        shuffle(deck)
        return deck

class Hand:
    DISCARDS = 3
    MAX_HAND_SIZE = 8

    def __init__(self):
        self.deck = Deck()
        self.cards = []
        self.discards_left = Hand.DISCARDS
        self.take_cards()

    def take_cards(self, quantity=None):

        if quantity is None:
            quantity = Hand.MAX_HAND_SIZE - len(self.cards)

        if not quantity:
            return

        cards_taken = self.deck.cards[-quantity:]
        self.deck.cards = self.deck.cards[:-quantity]
        self.cards.extend(cards_taken)

    def print_cards(self):
        for i, card in enumerate(self.cards):
            print(f'{i+1}{ (len(self.cards[i]) - 1) * " "}', end='  ')
        print()
        for card in self.cards:
            print(card, end='  ')
        print()

    def can_keep_playing(self):
        if self.discards_left == 0:
            return False
        else:
            return None

    def evaluated_win(self):
        suit_count = {}
        for card in self.cards:
            if card.suit not in suit_count:
                suit_count[card.suit] = 1
            else:
                suit_count[card.suit] += 1

        suit_repetitions = max(suit_count.values())
        if suit_repetitions < 5:
            # print('dont have 5')
            return self.can_keep_playing()

        # print(f'u got {suit_repetitions} reps')

        for key, value in suit_count.items():
            # Because hand size is 8 and flush is done with 5 cards, only one
            # match is possible, so I can just break
            if value == suit_repetitions:
                flush_suit = key
                break

        # print(f'they are {suit_repetitions}')

        flush_cards = []
        for card in self.cards:
            if card.suit == flush_suit:
                flush_cards.append(card.value)
        flush_cards.sort()
        points = sum(flush_cards[:5])

        print(f'Current sum: {points}')
        
        if points >= 40:
            return True
        else:
            return self.can_keep_playing()





hand = Hand()

while True:
    hand.print_cards()

    win_state = hand.evaluated_win()
    if win_state:
        print('You win!')
        break
    elif win_state is False:
        print('You loose.')
        break

    print(f'Start discarding ({hand.discards_left} left)')
    discard_indices = []
    for i in range(5):
        command = input(f'({i + 1} / 5) > ')
        if not command:
            break
        discard_indices.append(int(command) - 1)

    discard_indices.sort(reverse=True)
    for discard_index in discard_indices:
        hand.cards.pop(discard_index)

    hand.take_cards()

    hand.discards_left -= 1

    print('_' * 50, end='\n\n')

# deck = Deck()
#
# for card in deck.cards:
#     print(card)
#
#
