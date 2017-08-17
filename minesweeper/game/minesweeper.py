from minesweeper.game.board import Board


class Minesweeper():

    def __init__(self, width=10, height=10, bombs=10):
        self.width = width
        self.height = height
        self.bombs_number = bombs
        self.board = Board(width, height, bombs)

    def generate_board(self):
        self.board.generate()

    def get_board(self):
        return self.board

    def show(self):
        self.board.show()

    def reveal(self, block):
        self.board.reveal(block)

    def refresh(self):
        self.board.refresh()

    def reset(self):
        self.board.reset()
        self.refresh()

    def solve(self):
        for row in self.board:
            for block in row:
                if not block.is_bomb():
                    block.reveal()

    @property
    def finished(self):
        open_blocks = 0
        for row in self.board:
            for block in row:
                if block.is_visible:
                    open_blocks += 1

        if (open_blocks + self.bombs_number) == self.width * self.height:
            return True

        return False
