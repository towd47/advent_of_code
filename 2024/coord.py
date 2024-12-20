class Coord:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def fromCoord(coord):
        return Coord(coord.row, coord.col)

    def up(self):
        return Coord(self.row - 1, self.col)

    def down(self):
        return Coord(self.row + 1, self.col)

    def left(self):
        return Coord(self.row, self.col - 1)

    def right(self):
        return Coord(self.row, self.col + 1)

    def adjacent(self):
        return [self.up(), self.right(), self.down(), self.left()]

    def inBounds(self, rows, cols, row_min=0, col_min=0):
        return self.row < rows and self.col < cols and self.row >= row_min and self.col >= col_min

    def add(self, coord):
        return Coord(self.row + coord.row, self.col + coord.col)

    def sub(self, coord):
        return Coord(self.row - coord.row, self.col - coord.col)
        
    def val(self, grid):
        return grid[self.row][self.col]

    def cUp(coord):
        return coord.up()

    def cDown(coord):
        return coord.down()

    def cLeft(coord):
        return coord.left()

    def cRight(coord):
        return coord.right()

    def mDist(self, coord):
        return abs(self.row - coord.row) + abs(self.col - coord.col)

    def coordsAtDist(self, dist):
        crds = []
        for i in range(1, dist):
            c1 = Coord(dist - i, i)
            c2 = Coord(dist - i, i * -1)
            crds.append(self.add(c1))
            crds.append(self.sub(c1))
            crds.append(self.add(c2))
            crds.append(self.sub(c2))
        c1 = Coord(dist, 0)
        c2 = Coord(0, dist)
        crds.append(self.add(c1))
        crds.append(self.sub(c1))
        crds.append(self.add(c2))
        crds.append(self.sub(c2))
        return crds

    def __str__(self):
        return f"{self.row}, {self.col}"

    def __eq__(self, coord):
        return self.row == coord.row and self.col == coord.col

    def __lt__(self, other):
        if self.row == other.row:
            return self.col < other.col
        return self.row < other.row

    def __attrs(self):
        return (self.row, self.col)

    def __hash__(self):
        return hash(self.__attrs())
