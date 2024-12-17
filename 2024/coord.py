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

    def __str__(self):
        return f"{self.row}, {self.col}"

    def __eq__(self, coord):
        return self.row == coord.row and self.col == coord.col

    def __attrs(self):
        return (self.row, self.col)

    def __hash__(self):
        return hash(self.__attrs())
