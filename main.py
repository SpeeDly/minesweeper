import sys
from PyQt5.QtWidgets import QApplication
from minesweeper.ui.pyqt_ui import QMinesweeper
from minesweeper.game.minesweeper import Minesweeper


if __name__ == "__main__":
    application = QApplication(sys.argv)
    qMineSweeper = QMinesweeper(Minesweeper, 10, 10, 10)
    sys.exit(application.exec_())
