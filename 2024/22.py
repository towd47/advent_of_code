from readInput import yieldLines
import sys

def solve(filename='22'):
    lines = yieldLines(filename)
    print(sum([nextNSecrets(int(secret.strip()), 2000) for secret in lines]))

def nextNSecrets(secret, n):
    [secret := nextSecret(secret) for _ in range(n)]
    return secret

def nextSecret(secret):
    secret = (secret ^ (secret * 64)) % 16777216
    secret = (secret ^ (secret // 32)) % 16777216
    secret = (secret ^ (secret * 2048)) % 16777216
    return secret

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        solve(sys.argv[1])
    else:
        solve()


# 14337231886 high
