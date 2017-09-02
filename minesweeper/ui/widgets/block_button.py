from PyQt5.QtCore import Qt, QSize, QTimer
from PyQt5.QtWidgets import QPushButton, QSizePolicy


HINT_COLOR = 'rgb(250,250,210)'


class QBlockButton(QPushButton):

    def __init__(self, *args, **kwargs):
        super(QBlockButton, self).__init__(*args, **kwargs)
        self.setFocusPolicy(Qt.NoFocus)
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        self._color = 'None'

    def getColor(self):
        return self._color

    def setColor(self, color):
        self.setStyleSheet('background-color: {}'.format(color))
        self._color = color

    def resizeEvent(self, resizeEvent):
        font = self.font()
        font.setBold(True)
        font.setPixelSize(0.50 * min(self.width(), self.height()))
        self.setFont(font)

    def updateEvent(self, block, hint=False):
        if hint:
            # It will be better with animation, but I failed to do that :/
            self.setColor(HINT_COLOR)
            QTimer.singleShot(1000, lambda self=self: self.setColor('None'))

        if block.is_visible or block.marked:
            self.setText(str(block))

    def sizeHint(self):
        return QSize(35, 35)

    def on_left_click(self, func, *args, **kwargs):
        self.clicked.connect(
            lambda: func(*args, **kwargs))

    def on_right_click(self, func, *args, **kwargs):
        self.customContextMenuRequested.connect(
            lambda: func(*args, **kwargs))
