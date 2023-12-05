from PyQt5 import uic
from PyQt5.QtWidgets import *
import sqlite3
import sys


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.connection = sqlite3.connect('coffee.sqlite')
        self.cur = self.connection.cursor()
        self.add.clicked.connect(self.add_coffee)
        self.ids = self.cur.execute("""SELECT ID FROM coffee""").fetchall()

    def add_coffee(self):
        self.sort_name = self.sort.text()
        self.roast_name = self.degree.text()
        self.beans = self.ground.text()
        self.price_name = self.price.text()
        self.volume_name = self.volume.text()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())