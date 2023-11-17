import sys
from random import randint

from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton


class InterFace(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('Form')
        self.create_c = QPushButton('Create circle', self)
        self.create_c.move(190, 15)
        self.create_c.resize(120, 35)


class Circle(InterFace):
    def __init__(self):
        super().__init__()

        self.do_paint = False
        self.create_c.clicked.connect(self.paint)

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
        pen = QPen(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
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
