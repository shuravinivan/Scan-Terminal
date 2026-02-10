from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle('Сканер терминала')
        self.setGeometry(100, 100, 800, 600)

        self.new_text = QtWidgets.QLabel(self)

        self.main_text = QtWidgets.QLabel(self)
        self.main_text.setText("Основная надпись")
        self.main_text.move(100, 100)
        self.main_text.adjustSize()

        self.btn = QtWidgets.QPushButton(self)
        self.btn.move(500, 500)
        self.btn.setText('Нажми тут')
        self.btn.setFixedWidth(200)
        self.btn.clicked.connect(self.add_label)

    def add_label(self):
        self.new_text.setText('Вторая надпись')
        self.move(100, 50)
        self.adjustSize()
        self.setGeometry(100, 100, 800, 600)

def application():
    app = QApplication(sys.argv)
    window = Window()



    window.show()
    sys.exit(app.exec_())
application()