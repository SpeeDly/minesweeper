from random import randint

from minesweeper.game.block import Block
from minesweeper.game.exceptions import GameNotStarted


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

    def get_surrounding_blocks(self, block):
        surrounding_blocks = []
        top, left, bottom, right = self.get_top_block(block), self.get_left_block(block),\
            self.get_bottom_block(block), self.get_right_block(block)

        if top:
            surrounding_blocks.append(top)
            if self.get_right_block(top):
                surrounding_blocks.append(self.get_right_block(top))
            if self.get_left_block(top):
                surrounding_blocks.append(self.get_left_block(top))

        if bottom:
            surrounding_blocks.append(bottom)
            if self.get_right_block(bottom):
                surrounding_blocks.append(self.get_right_block(bottom))
            if self.get_left_block(bottom):
                surrounding_blocks.append(self.get_left_block(bottom))

        if left:
            surrounding_blocks.append(left)

        if right:
            surrounding_blocks.append(right)

        return surrounding_blocks

    def increase_surrounding_blocks(self, block):
        near_blocks = self.get_surrounding_blocks(block)
        for b in near_blocks:
            b.increase()

    def refresh(self):
        for row in self:
            for block in row:
                block.refresh()

    def generate_hint(self):
        block_to_risk = []

        for row in self.board:
            for block in row:
                if not block.is_visible:
                    risk = 0
                    near_blocks = self.get_surrounding_blocks(block)
                    for nb in near_blocks:
                        if nb.is_visible:
                            risk += nb.get_value()
                    if risk != 0:
                        block_to_risk.append((block, risk))

        if not block_to_risk:
            raise GameNotStarted

        block_to_risk.sort(key=lambda el: el[1])
        choosen_block = block_to_risk[0][0]
        choosen_block.hint()

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
