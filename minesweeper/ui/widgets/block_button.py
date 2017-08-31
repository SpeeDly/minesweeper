from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QPushButton, QSizePolicy


class QBlockButton(QPushButton):
    def __init__(self):
        super(QBlockButton, self).__init__()
        self.setFocusPolicy(Qt.NoFocus)
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)

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

    def on_left_click(self, func, block):
        self.clicked.connect(
            lambda: func(block))

    def on_right_click(self, func, block):
        self.customContextMenuRequested.connect(
            lambda: func(block))
