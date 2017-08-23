from unittest import mock

from minesweeper.game.board import Board


def test_generate():
    board = Board(10, 10, 10)
    board.generate()
    bombs = 0

    for row in board:
        for block in row:
            if block.is_bomb():
                bombs += 1

    assert bombs == 10


def test_position_getters():
    board = Board(10, 10, 10)
    board.generate()
    block = board.board[1][1]
    b1, b2, b3, b4 = board.get_top_block(block), board.get_right_block(block),\
        board.get_bottom_block(block), board.get_left_block(block)

    assert b1.get_coords() == (1, 0)
    assert b2.get_coords() == (2, 1)
    assert b3.get_coords() == (1, 2)
    assert b4.get_coords() == (0, 1)


def test_set_and_get():
    board = Board(10, 10, 10)
    board.generate()
    board[0] = 5
    assert board[0] == 5


@mock.patch('minesweeper.game.block.Block.refresh')
def test_refresh(mock_block):
    board = Board(10, 10, 10)
    board.generate()
    board.refresh()
    assert mock_block.call_count == 100


def test_reveal():
    board = Board(10, 10, 10)
    board.generate()
    board[0][0].set_value(0)
    board[0][1].set_value(1)
    board[0][2].make_bomb()
    board.reveal(board[0][0])
    assert board[0][0].is_visible
    assert board[0][1].is_visible
    assert not board[0][2].is_visible
