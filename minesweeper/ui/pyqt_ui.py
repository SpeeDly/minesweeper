import random

from PyQt5.QtWidgets import QWidget, QPushButton, QMessageBox, QGridLayout, QSizePolicy
from PyQt5.QtCore import Qt, QSize

from minesweeper.webui.webui import webUI


class QMinesweeper(QWidget):
    class QBlockButton(QPushButton):
        def __init__(self):
            super(QMinesweeper.QBlockButton, self).__init__()
            self.setFocusPolicy(Qt.NoFocus)
            self.setContextMenuPolicy(Qt.CustomContextMenu)
            self.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)

        def clickEvent(self, block):
            self.parent().reveal(block)

        def menuEvent(self, block):
            self.parent().mark(block)

        def resizeEvent(self, resizeEvent):
            font = self.font()
            font.setBold(True)
            font.setPixelSize(0.50 * min(self.width(), self.height()))
            self.setFont(font)

        def updateEvent(self, block):
            if block.is_visible or block.marked:
                self.setText(str(block))

        def sizeHint(self):
            return QSize(35, 35)

    def __init__(self, engine, width, height, bomb_number):
        super(QMinesweeper, self).__init__()
        self.minesweeper = engine(width, height, bomb_number)
        self.game_id = random.randint(1, 100000)
        self.initUI()
        self.show()
        self.minesweeper.show()
        webUI.init(self.game_id, self.minesweeper.serialize())

    def initUI(self):
        self.minesweeper.generate_board()
        self.setWindowTitle(self.tr("Minesweeper - " + str(self.game_id)))
        layout = QGridLayout()
        layout.setSpacing(11)
        self.setLayout(layout)

        for row in self.minesweeper.get_board():
            for block in row:
                coords = block.get_coords()
                button = QMinesweeper.QBlockButton()
                self.layout().addWidget(button, coords[0], coords[1])
                button.clicked.connect(lambda _, button=button, block=block: button.clickEvent(block))
                button.customContextMenuRequested.connect(lambda _, button=button, block=block: button.menuEvent(block))
                block.update = button.updateEvent

    def mark(self, block):
        block.toggle_mark()
        self.minesweeper.refresh()

    def reveal(self, block):
        self.minesweeper.reveal(block)
        self.minesweeper.refresh()
        webUI.update(self.game_id, self.minesweeper.serialize())

        if block.is_bomb():
            QMessageBox.critical(self, self.tr("Defeat!"), self.tr("You loose :("), QMessageBox.Ok)
            webUI.finish(self.game_id, -1)
            self.minesweeper.reset()

        if self.minesweeper.finished:
            QMessageBox.information(self, self.tr("Victory!"), self.tr("You win :)"), QMessageBox.Ok)
            webUI.finish(self.game_id, 1)
            self.minesweeper.reset()

    def sizeHint(self):
        return QSize(300, 300)
