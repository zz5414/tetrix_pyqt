import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QFrame

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import QBasicTimer

from PyQt5.QtGui import QPainter
from PyQt5.QtGui import QColor


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

        self.resize(180, 380)

        self.show()

class TetrisBoard(QFrame):
    msg_to_statusbar = pyqtSignal(str)

    Speed = 300
    BoardWidth = 10
    BoardHeight = 22



    def __init__(self, parent):
        super().__init__(parent)

        # member variable
        self.timer = QBasicTimer()

        self._test_int = 1

    def start(self):
        self.msg_to_statusbar.emit("Hello World")
        self.timer.start(TetrisBoard.Speed, self)

    def timerEvent(self, event):
        if event.timerId() == self.timer.timerId():
            self.msg_to_statusbar.emit(str(self._test_int))
            self._test_int += 1
            self.update()
        else:
            super(TetrisBoard, self).timerEvent(event)

    def paintEvent(self, event):
        painter = QPainter(self)
        rect = self.contentsRect()

        #가장 아랫부분까지 채울 수 있도록 정해진 크기만큼 height를 가지도록 윗부분을 자른다.(특정 윗부분을 사용하지 않겠다는 의미)
        boardTop = rect.height() - TetrisBoard.BoardHeight * self.squareHeight()

        for h_index in range(TetrisBoard.BoardHeight):
            for w_index in range(TetrisBoard.BoardWidth):
                import random
                shape = random.randint(1, 7)
                colorTable = [0x000000, 0xCC6666, 0x66CC66, 0x6666CC,
                              0xCCCC66, 0xCC66CC, 0x66CCCC, 0xDAAA00]
                x = rect.left() + w_index * self.squareWidth()
                y = boardTop + h_index * self.squareHeight()
                painter.fillRect(x, y, self.squareWidth(), self.squareHeight(), QColor(colorTable[shape]))



    def squareWidth(self):
        '''returns the width of one square'''
        # print(self.contentsRect().width(), TetrisBoard.BoardWidth, self.contentsRect().width() // TetrisBoard.BoardWidth)
        return self.contentsRect().width() // TetrisBoard.BoardWidth

    def squareHeight(self):
        '''returns the height of one square'''
        # print(self.contentsRect().height(), TetrisBoard.BoardHeight, self.contentsRect().height() // TetrisBoard.BoardHeight)
        return self.contentsRect().height() // TetrisBoard.BoardHeight



if __name__ == "__main__":
    app = QApplication([])
    tetris = Tetris()
    sys.exit(app.exec_())
