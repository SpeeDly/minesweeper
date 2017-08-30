from random import randint

from minesweeper.game.block import Block


class Board():

    def __init__(self, width, height, bombs_number):
        self.width = width
        self.height = height
        self.bombs_number = bombs_number
        self.board = [[Block((row, col)) for col in range(width)] for row in range(height)]

    def __iter__(self):
        return iter(self.board)

    def __getitem__(self, index):
        return self.board[index]

    def __setitem__(self, index, value):
        self.board[index] = value

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

    def get_top_block(self, block):
        coords = block.get_coords()
        if coords[1] - 1 >= 0:
            return self.board[coords[0]][coords[1] - 1]

    def get_bottom_block(self, block):
        coords = block.get_coords()
        if coords[1] + 1 < self.height:
            return self.board[coords[0]][coords[1] + 1]

    def get_left_block(self, block):
        coords = block.get_coords()
        if coords[0] - 1 >= 0:
            return self.board[coords[0] - 1][coords[1]]

    def get_right_block(self, block):
        coords = block.get_coords()
        if coords[0] + 1 < self.width:
            return self.board[coords[0] + 1][coords[1]]

    def increase_surrounding_blocks(self, block):
        top, left, bottom, right = self.get_top_block(block), self.get_left_block(block),\
            self.get_bottom_block(block), self.get_right_block(block)

        if top:
            top.increase()
            if self.get_right_block(top):
                self.get_right_block(top).increase()
            if self.get_left_block(top):
                self.get_left_block(top).increase()

        if bottom:
            bottom.increase()
            if self.get_right_block(bottom):
                self.get_right_block(bottom).increase()
            if self.get_left_block(bottom):
                self.get_left_block(bottom).increase()

        if left:
            left.increase()

        if right:
            right.increase()

    def refresh(self):
        for row in self:
            for block in row:
                block.refresh()

    def show(self):
        for row in self:
            print(row)

    def reveal(self, block):
        block.reveal()
        if block.get_value() == 0:
            blocks = [self.get_top_block(block), self.get_left_block(block),
                      self.get_bottom_block(block), self.get_right_block(block)]

            for b in blocks:
                if b and not b.is_bomb() and not b.is_visible:
                    self.reveal(b)

    def reset(self):
        for row in self:
            for block in row:
                block.reset()

    def serialize(self):
        board = []

        for row in self.board:
            r = []
            for block in row:
                r.append(block.serialize())
            board.append(r)

        return board
