import readInput

def day4():
    cards = readInput.linesToList("4")
    part1(cards)
    part2(cards)

def cardMatches(card):
    card = card.strip()
    nums = card.split(":")[1]
    winningNums, scratchNums = nums.split("|")

    winningNums = set([int(x) for x in winningNums.split()])
    scratchNums = set([int(x) for x in scratchNums.split()])

    winners = winningNums & scratchNums
    return len(winners)
    
def part1(cards):
    points = 0
    for card in cards:
        numMatches = cardMatches(card)
        if numMatches > 0:
            points += 2 ** (numMatches - 1)

    print(points)

def part2(cards):
    cardCounts = [1] * len(cards)

    for i, card in enumerate(cards):
        numMatches = cardMatches(card)
        copies = list(range(i + 1, i + numMatches + 1))
        for x in copies:
            if x < len(cardCounts):
                cardCounts[x] += cardCounts[i]

    print(sum(cardCounts))

if __name__ == "__main__":
    day4()