import readInput
from functools import cmp_to_key

def cardToVal(card):
    if card == "A": return 14
    if card == "K": return 13
    if card == "Q": return 12
    if card == "J": return 11
    if card == "T": return 10
    return int(card)

def jIsWild(card):
    if card == "J": return 1
    return card

def handToList(cards):
    return [cardToVal(x) for x in cards]

def handToListP2(cards):
    return [cardToVal(jIsWild(x)) for x in cards]

def compareCards(c1, c2):
    c1 = c1[0]
    c2 = c2[0]
    if handScore(c1) > handScore(c2):
        return 1
    if handScore(c1) < handScore(c2):
        return -1
    for x, y in zip(c1, c2):
        if x - y != 0:
            return x - y
    return 0

def compareCardsP2(c1, c2):
    c1 = c1[0]
    c2 = c2[0]

    if handScoreP2(c1) > handScoreP2(c2):
        return 1
    if handScoreP2(c1) < handScoreP2(c2):
        return -1
    for x, y in zip(c1, c2):
        if x - y != 0:
            return x - y
    return 0

def handScore(hand):
    handSet = set(hand)
    setCount = len(handSet)

    if setCount == 1: return 6
    if setCount == 2:
        for x in handSet:
            if hand.count(x) == 4:
                return 5
        return 4
    if setCount == 3:
        for x in handSet:
            if hand.count(x) == 3:
                return 3
        return 2
    if setCount == 4:
        return 1
    return 0

def handScoreP2(hand):
    if 1 not in hand:
        return handScore(hand)
    
    cards = set(hand)
    cards.remove(1)

    setCount = len(cards)
    if setCount == 0 or setCount == 1: return 6
    if setCount == 2:
        for x in cards:
            if hand.count(x) < 2 or hand.count(x) > 2: return 5
        return 4
    if setCount == 3: return 3
    return 1

cards = []
cardsP2 = []
for line in readInput.yieldLines("7"):
    line = line.strip()
    hand, bet = line.split()
    cards.append((handToList(hand), int(bet)))
    cardsP2.append((handToListP2(hand), int(bet)))

sortedCards = sorted(cards, key=cmp_to_key(compareCards))
totalWinnings = 0
for rank, card in enumerate(sortedCards):
    totalWinnings += (rank + 1) * card[1]

print(totalWinnings)

sortedCardsP2 = sorted(cardsP2, key=cmp_to_key(compareCardsP2))

totalWinnings = 0
for rank, card in enumerate(sortedCardsP2):
    totalWinnings += (rank + 1) * card[1]

print(totalWinnings)