from tabulate import tabulate
import random

def makeDeck():
    suits = ["Hearts", "Spades", "Diamonds", "Clubs"]
    values = list(range(1, 14))
    deck = []
    for suit in suits:
        for value in values:
            deck.append({"suit": suit, "value": value})
    return deck

def prettyFormat(card):
    names = {1: "Ace", 11: "Jack", 12: "Queen", 13: "King"}
    val = names.get(card["value"], str(card["value"]))
    return f"{val} of {card['suit']}"

def deal(deck, cards_per_hand, num_hands):
    total = cards_per_hand * num_hands
    if total > len(deck):
        print("Not enough cards in deck")
        return []
    if cards_per_hand <= 0 or num_hands <= 0:
        print("Invalid input")
        return []
    random.shuffle(deck)
    hands = []
    for hand_index in range(num_hands):
        hand = []
        for card_index in range(cards_per_hand):
            card = deck.pop()
            hand.append(card)
        hands.append(hand)
    return hands

def displayHands(hands):
    for index in range(len(hands)):
        hand = hands[index]
        table = []
        for i in range(len(hand)):
            table.append([i + 1, prettyFormat(hand[i])])
        print(f"\nHand {index + 1}:")
        print(tabulate(table, headers=["#", "Card"], tablefmt="grid"))

def main():
    deck = makeDeck()
    hands = deal(deck, 5, 2)
    if hands:
        displayHands(hands)
        print(f"\nCards remaining in deck: {len(deck)}")

main()
