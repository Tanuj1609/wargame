import random

# Define the card ranks and suits
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}

# Card class
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"

# Deck class
class Deck:
    def __init__(self):
        self.deck = [Card(suit, rank) for suit in suits for rank in ranks]

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()

# Player class
class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def add_cards(self, new_cards):
        if isinstance(new_cards, list):
            self.cards.extend(new_cards)
        else:
            self.cards.append(new_cards)

    def remove_card(self):
        return self.cards.pop(0)

# Function to play a single round of War
def play_round(player1, player2):
    print(f"\n{player1.name} plays {player1.cards[0]}")
    print(f"{player2.name} plays {player2.cards[0]}")

    if player1.cards[0].value > player2.cards[0].value:
        print(f"{player1.name} wins this round!")
        player1.add_cards([player1.remove_card(), player2.remove_card()])
    elif player1.cards[0].value < player2.cards[0].value:
        print(f"{player2.name} wins this round!")
        player2.add_cards([player1.remove_card(), player2.remove_card()])
    else:
        print("War!")
        war(player1, player2)

# Function to handle War scenario
def war(player1, player2):
    if len(player1.cards) < 4 or len(player2.cards) < 4:
        if len(player1.cards) < 4:
            print(f"{player1.name} cannot continue the war and loses!")
            player2.add_cards(player1.cards)
            player1.cards = []
        else:
            print(f"{player2.name} cannot continue the war and loses!")
            player1.add_cards(player2.cards)
            player2.cards = []
        return

    war_cards_p1 = [player1.remove_card() for _ in range(4)]
    war_cards_p2 = [player2.remove_card() for _ in range(4)]

    print(f"{player1.name} puts {war_cards_p1[-1]} as war card")
    print(f"{player2.name} puts {war_cards_p2[-1]} as war card")

    if war_cards_p1[-1].value > war_cards_p2[-1].value:
        print(f"{player1.name} wins the war!")
        player1.add_cards(war_cards_p1 + war_cards_p2)
    elif war_cards_p1[-1].value < war_cards_p2[-1].value:
        print(f"{player2.name} wins the war!")
        player2.add_cards(war_cards_p1 + war_cards_p2)
    else:
        print("War continues!")
        war(player1, player2)

# Main game logic
def play_game():
    print("Welcome to the War card game!")

    # Create and shuffle the deck
    deck = Deck()
    deck.shuffle()

    # Create two players
    player1 = Player("Player 1")
    player2 = Player("Player 2")

    # Deal the cards to the players
    while len(deck.deck) > 0:
        player1.add_cards(deck.deal())
        player2.add_cards(deck.deal())

    # Play the game
    round_number = 1
    while len(player1.cards) > 0 and len(player2.cards) > 0:
        print(f"\n--- Round {round_number} ---")
        play_round(player1, player2)
        round_number += 1

    # Determine the winner
    if len(player1.cards) > 0:
        print(f"\n{player1.name} wins the game!")
    else:
        print(f"\n{player2.name} wins the game!")

# Start the game
if __name__ == "__main__":
    play_game()
