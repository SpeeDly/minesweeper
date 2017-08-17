from minesweeper.game.block import Block


def test_set_value():
    block = Block()
    block.set_value(5)
    assert block.get_value() == 5


def test_make_bomb():
    block = Block()
    block.make_bomb()
    assert block.is_bomb()


def test_reveal():
    block = Block()
    block.reveal()
    assert block.is_visible


def test_toggle_mark():
    block = Block()
    block.toggle_mark()
    assert block.is_marked()

    block.toggle_mark()
    assert not block.is_marked()


def test_get_coords():
    block = Block((0, 0))
    assert block.get_coords() == (0, 0)


def test_increase():
    block = Block()
    block.increase()
    assert block.get_value() == 1


def test_refresh():
    block = Block()
    block.refresh()


def test_to_string():
    block = Block()
    assert str(block) == '0'

    block.make_bomb()
    assert str(block) == 'B'

    block.toggle_mark()
    assert str(block) == 'X'
