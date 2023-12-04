import readInput

# 537272 < x < 539127

lines = readInput.linesToList("3")
lines = [x.strip() for x in lines]

grid = zip(list(range(len(lines))), lines)
grid = list(grid)

symbols = dict()
stars = []
nums = []
for rownum, row in grid:
    num = ""
    p0 = 0
    for n, c in enumerate(row):
        if n == len(row) - 1 or not c.isdigit():
            if c.isdigit():
                if not num:
                    p0 = n - 1
                num += c
            if num != "":
                p1 = n
                nums.append((rownum, int(num), p0, p1))
                num = ""
            if not c == '.' and not c.isdigit():
                if c == "*":
                    stars.append((rownum, n))
                if rownum in symbols:
                    symbols[rownum].append(n)
                else:
                    symbols[rownum] = [n]
        else:
            if not num:
                p0 = n - 1
            num += c

tot = 0
for row, n, p0, p1 in nums:
    for i in range(row - 1, row + 2):
        if i in symbols:
            symbolRow = symbols[i]
            found = False
            for e in symbolRow:
                if e >= p0 and e <= p1:
                    tot += n
                    found = True
                    break
            if found:
                break

print(tot)

ratioTot = 0
for star in stars:
    adj = []
    for num in nums:
        if star[0] in range(num[0]-1, num[0]+2) and star[1] >= num[2] and star[1] <= num[3]:
            adj.append(num[1])
    if len(adj) == 2:
        ratioTot += adj[0] * adj[1]

print(ratioTot)


