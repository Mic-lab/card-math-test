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

    def count_suits(self):
        suit_count = {}
        for card in self.cards:
            if card.suit not in suit_count:
                suit_count[card.suit] = 1
            else:
                suit_count[card.suit] += 1
        return suit_count

    def evaluated_win(self):
        suit_count = self.count_suits()
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

def percent(a, b):
    return f'{round(a/b * 100, 4)} %'

SIMULATIONS = 1_000_000

def simulate():
    hand = Hand()
    
    suit_count = hand.count_suits()
    target_suit_count = max(suit_count.values())
    
    for k, v in suit_count.items():
        if v == target_suit_count:
            target_suit = k

    # hand.print_cards()
    # print(target_suit_count, target_suit)

    discards = 0
    while True:
        # hand.print_cards()

        good_cards = 0
        bad_cards = 0

        new_cards = []

        for card in hand.cards:

            if card.suit == target_suit:
                good_cards += 1
                new_cards.append(card)
            else:
                bad_cards += 1

        if good_cards >= 5:
            return True, discards
        elif bad_cards == 5:
            pass
            # print('did all i can, next')

        hand.cards = new_cards 
        hand.take_cards()
        discards += 1

        # print('after:')
        # hand.print_cards()

        # if discards == 3:
        if discards == 4:
            return False, discards

        # print('_' * 50, end='\n\n')
        # input('>')

games = {0: [0, 0],
         1: [0, 0],
         2: [0, 0],
         3: [0, 0]}

next_percent = 0
for i in range(SIMULATIONS):
    win, discards = simulate()
    games[discards][int(win)] += 1
    
    if i / SIMULATIONS >= next_percent:
        print(percent(i, SIMULATIONS))
        next_percent += 0.1
    # print('lesgo' if win else 'dam')
    # print(f'{discards=}')
    # input('new simulation > ')

print(f'{SIMULATIONS=}')
print(games)
for k, v in games.items():
    print(f'{k} discards:')
    if v[1] + v[0] == 0:
        p1 = 'na'
    else:
        p1 = percent(v[1], v[1] + v[0])
    p2 = percent(v[1], SIMULATIONS)
    print(f'    Conditional odds   {p1}')
    print(f'    Unconditional odds {p2}')

