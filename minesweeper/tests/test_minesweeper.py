from unittest import mock

from minesweeper.game.block import Block
from minesweeper.game.minesweeper import Minesweeper


@mock.patch('minesweeper.game.board.Board.generate')
def test_generate_board(mock_board):
    m = Minesweeper()
    m.generate_board()
    assert mock_board.call_count == 1


@mock.patch('minesweeper.game.board.Board.reveal')
def test_reveal(mock_board):
    m = Minesweeper()
    b = Block()
    m.reveal(b)
    assert mock_board.call_count == 1


@mock.patch('minesweeper.game.board.Board.refresh')
def test_refresh(mock_board):
    m = Minesweeper()
    m.refresh()
    assert mock_board.call_count == 1


@mock.patch('minesweeper.game.board.Board.generate')
def test_reset(mock_board):
    m = Minesweeper()
    m.generate_board()
    assert mock_board.call_count == 1


def test_not_finished():
    m = Minesweeper()
    m.generate_board()
    assert not m.finished


def test_finished():
    m = Minesweeper()
    m.generate_board()
    m.solve()
    assert m.finished
