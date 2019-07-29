import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QFrame

from PyQt5.QtCore import pyqtSignal


class Tetris(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        tetris_board = TetrisBoard(self)
        self.setCentralWidget(tetris_board)

        self.status_bar = self.statusBar()
        tetris_board.msg_to_statusbar.connect(self.status_bar.showMessage)

        tetris_board.start()

        self.show()

class TetrisBoard(QFrame):
    msg_to_statusbar = pyqtSignal(str)

    def __init__(self, parent):
        super().__init__(parent)

    def start(self):
        self.msg_to_statusbar.emit("Hello World")


if __name__ == "__main__":
    app = QApplication([])
    tetris = Tetris()
    sys.exit(app.exec_())
