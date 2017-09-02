import random

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QWidget, QMessageBox, QGridLayout

from minesweeper.webui.webui import webUI
from minesweeper.game.exceptions import GameNotStarted
from minesweeper.ui.widgets import QBlockButton


class QMinesweeperGame(QWidget):

    def __init__(self, engine, width, height, bomb_number):
        super(QMinesweeperGame, self).__init__()
        self.minesweeper = engine(width, height, bomb_number)
        self.minesweeper.generate_board()
        self.game_id = random.randint(1, 100000)
        self.width = width
        self.height = height
        self.initUI()
        self.show()
        self.minesweeper.show()
        webUI.init(self.game_id, self.minesweeper.serialize())

    def initUI(self):
        self.setWindowTitle(self.tr("Minesweeper - " + str(self.game_id)))

        layout = QGridLayout()
        layout.setSpacing(11)
        self.setLayout(layout)

        hint_button = QBlockButton('?')
        self.layout().addWidget(hint_button, 0, self.width - 1)
        hint_button.setToolTip('Hint')
        hint_button.setStyleSheet('margin-bottom: 10px')
        hint_button.on_left_click(self.generate_hint)

        for row in self.minesweeper.get_board():
            for block in row:
                coords = block.get_coords()
                button = QBlockButton()
                self.layout().addWidget(button, coords[0] + 2, coords[1])
                button.on_left_click(self.reveal, block)
                button.on_right_click(self.mark, block)
                block.update = button.updateEvent

    def closeEvent(self, event):
        if not self.minesweeper.finished:
            webUI.finish(self.game_id, -1)
        event.accept()

    def mark(self, block):
        block.toggle_mark()
        self.minesweeper.refresh()

    def reveal(self, block):
        self.minesweeper.reveal(block)
        self.minesweeper.refresh()
        webUI.update(self.game_id, self.minesweeper.serialize())

        if block.is_bomb():
            QMessageBox.critical(
                self, self.tr("Defeat!"), self.tr("You loose :("), QMessageBox.Ok)
            webUI.finish(self.game_id, -1)
            self.minesweeper.reset()

        if self.minesweeper.finished:
            QMessageBox.information(
                self, self.tr("Victory!"), self.tr("You win :)"), QMessageBox.Ok)
            webUI.finish(self.game_id, 1)
            self.minesweeper.reset()

    def generate_hint(self):
        try:
            self.minesweeper.generate_hint()
        except GameNotStarted:
            QMessageBox.information(
                self, self.tr("Error!"), self.tr("The game is not started yet!"), QMessageBox.Ok)

    def sizeHint(self):
        return QSize(300, 300)
