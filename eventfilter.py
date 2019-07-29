import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.label = QLabel(self)
        self.label.setText('Hello World')
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFrameStyle(QFrame.Box | QFrame.Plain)
        self.label.setMouseTracking(True)
        self.label.installEventFilter(self)
        layout = QVBoxLayout(self)
        layout.addWidget(self.label)

    def eventFilter(self, source, event):
        if (event.type() == QEvent.MouseMove and
            source is self.label):
            pos = event.pos()
            print('mouse move: (%d, %d)' % (pos.x(), pos.y()))
        return QWidget.eventFilter(self, source, event)

if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    window.resize(200, 100)
    sys.exit(app.exec_())