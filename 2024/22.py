from readInput import yieldLines
import sys

def solve(filename='22'):
    lines = yieldLines(filename)
    lines = [int(line.strip()) for line in lines]
    print(sum([nextNSecrets(secret, 2000) for secret in lines]))
    diffMap = {}
    for secret in lines:
        dm = genDiffMap(secret, 1999)
        for key in dm:
            if key in diffMap:
                diffMap[key] += dm[key]
            else:
                diffMap[key] = dm[key]

    print(max(diffMap.values()))

def nextNSecrets(secret, n):
    [secret := nextSecret(secret) for _ in range(n)]
    return secret

def nextSecret(secret):
    secret = (secret ^ (secret * 64)) % 16777216
    secret = (secret ^ (secret // 32)) % 16777216
    secret = (secret ^ (secret * 2048)) % 16777216
    return secret

def genDiffMap(secret, n):
    diffs = []
    diffMap = {}
    for i in range(n):
        s = secret
        s1 = nextSecret(secret)
        diffs.append(s1 % 10 - s % 10)
        if len(diffs) == 4:
            diffTup = tuple(diffs)
            if diffTup not in diffMap:
                diffMap[diffTup] = s1 % 10
            diffs.pop(0)
        secret = s1
    return diffMap

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        solve(sys.argv[1])
    else:
        solve()


# 14337231886 high
# 903 low
# 1715 high
