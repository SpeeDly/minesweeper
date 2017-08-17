from random import randint


class Block():

    def __init__(self, coords=None):
        self.coords = coords
        self.value = 0
        self.is_visible = False

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def click(self):
        self.is_visible = True

    def make_bomb(self):
        self.value = -1

    def is_bomb(self):
        return self.value == -1

    def increase(self, number=1):
        if not self.is_bomb():
            self.value += number

    def get_coords(self):
        return self.coords

    def __repr__(self):
        if self.is_bomb():
            return 'B'
        return str(self.get_value())


class Board():

    def __init__(self, width, height, bombs_number):
        self.width = width
        self.height = height
        self.bombs_number = bombs_number
        self.board = [[Block((row, col)) for col in range(width)] for row in range(height)]

    def generate(self):
        placed_bombs = 0
        while not placed_bombs == self.bombs_number:
            rand1, rand2 = randint(0, self.width - 1), randint(0, self.height - 1)
            if not self.board[rand1][rand2].is_bomb():
                self.board[rand1][rand2].make_bomb()
                placed_bombs += 1

        for row in self.board:
            for b in row:
                if b.is_bomb():
                    self.increase_surrounding_blocks(b)

    def increase_surrounding_blocks(self, block):
        coords = block.get_coords()
        # left
        if coords[0] - 1 >= 0:
            self.board[coords[0] - 1][coords[1]].increase()
            # top left
            if coords[1] - 1 >= 0:
                self.board[coords[0] - 1][coords[1] - 1].increase()
            # bottom left
            if coords[1] + 1 < self.height:
                self.board[coords[0] - 1][coords[1] + 1].increase()

        # right
        if coords[0] + 1 < self.width:
            self.board[coords[0] + 1][coords[1]].increase()
            # top right
            if coords[1] - 1 >= 0:
                self.board[coords[0] + 1][coords[1] - 1].increase()
            # bottom right
            if coords[1] + 1 < self.height:
                self.board[coords[0] + 1][coords[1] + 1].increase()
        # top
        if coords[1] - 1 >= 0:
            self.board[coords[0]][coords[1] - 1].increase()
        # bottom
        if coords[1] + 1 < self.height:
            self.board[coords[0]][coords[1] + 1].increase()

    def show(self):
        for row in self.board:
            print(row)


class Minesweeper():

    def __init__(self, width=10, height=10, bombs=10):
        self.width = width
        self.height = height
        self.bombs_number = bombs
        self.board = Board(width, height, bombs)

    def generate_board(self):
        self.board.generate()

    def show(self):
        self.board.show()
