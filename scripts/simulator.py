from random import shuffle

fg = lambda text, color: "\33[38;5;" + str(color) + "m" + text + "\33[0m"
bg = lambda text, color: "\33[48;5;" + str(color) + "m" + text + "\33[0m"

def dprint(*args, **kwargs):
    if DEBUG: print(*args, **kwargs)

def dinput(*args):
    if DEBUG: input(*args)

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
        return f'{self.rank} {self.style["symbol"]}'

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
            dprint(f'{i+1}{ (len(self.cards[i]) - 1) * " "}', end='  ')
        dprint()
        for card in self.cards:
            dprint(card, end='  ')
        dprint()

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

def simulate():

    hand = Hand()
    suit_count = hand.count_suits()
    target_suit_reps = max(suit_count.values())

    for target_suit, reps in suit_count.items():
        if reps == target_suit_reps:
            break

    hand.print_cards()
    dprint(f'{target_suit=} {target_suit_reps=}\n')

    for discards in range(4):

        new_cards = []
        bad_cards = 0
        good_cards = 0
        for card in hand.cards:
            if card.suit == target_suit:
                good_cards += 1
                new_cards.append(card)
            else:
                ########
                if bad_cards >= 5:
                    new_cards.append(card)
                ########
                bad_cards += 1

            if good_cards == 5:
                return True, discards


        hand.cards = new_cards
        hand.take_cards()

        dprint('New state : ')
        hand.print_cards()
        dinput('> ')

    return False, discards

SIMULATIONS = 1_000_000
DEBUG = False

all_wins = {
    0: 0,
    1: 0,
    2: 0,
    3: 0}

next_completion_ratio = 0
for i in range(SIMULATIONS):
    completion_ratio = i / SIMULATIONS
    if completion_ratio >= next_completion_ratio:
        next_completion_ratio += 0.1
        print(round(completion_ratio * 100), '%')
    win, discards = simulate()
    dprint('WIN' if win else 'LOSS', discards)
    dinput('------------------------------------\n> ')
    all_wins[discards] += int(win)

for discard, wins in all_wins.items():
    print(f'{discard} Discards: {wins}/{SIMULATIONS} = {round(wins/SIMULATIONS * 100, 4)} %')

print(f'Odds of loosing {(all_wins[0] + all_wins[1] + all_wins[2] + all_wins[3]) / SIMULATIONS * 100}')

# deck = Deck()
#
# for card in deck.cards:
#     print(card)
#
#
