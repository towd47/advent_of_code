import readInput

def readGrid(f):
    return [list(map(int, list(x))) for x in readInput.linesToList(f)]

def solve():
    grid = readGrid("tests")
    
if __name__ == "__main__":
    solve()