import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt
from random import randint
from PyQt5.uic import loadUi


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('UI.ui', self)
        self.button.clicked.connect(self.on_button_click)

    def on_button_click(self):
        self.update()

    def paintEvent(self, event):
        qp = QPainter(self)
        qp.setBrush(QColor(255, 255, 0))  # Yellow color
        diameter = randint(10, 100)  # Random diameter
        x = randint(0, self.width() - diameter)
        y = randint(0, self.height() - diameter)
        qp.drawEllipse(x, y, diameter, diameter)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
