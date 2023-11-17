import sys
from random import randint

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtWidgets import QWidget, QApplication


class Circle(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)
        self.do_paint = False
        self.create.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_circle(self, qp):
        pen = QPen(QColor(255, 255, 0))
        pen.setWidth(5)
        qp.setPen(pen)

        x, y = randint(50, 300), randint(50, 300)
        w = randint(50, 500 - max(x, y))
        qp.drawEllipse(x, y, w, w)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Circle()
    ex.show()
    sys.exit(app.exec())
