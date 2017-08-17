import sys
from PyQt5.QtWidgets import QApplication
from ui.pyqt_ui import QMinesweeper


if __name__ == "__main__":
    application = QApplication(sys.argv)
    qMineSweeper = QMinesweeper(10)
    sys.exit(application.exec_())
