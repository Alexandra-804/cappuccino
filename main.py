import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
import sqlite3


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.connection = sqlite3.connect('coffee.sqlite')
        self.cur = self.connection.cursor()
        self.search.clicked.connect(self.run)


    def run(self):
        self.s = self.select.currentText()
        self.choose = self.type.text()
        if self.s == 'ID':
            self.find = self.cur.execute(f"""SELECT * FROM coffee WHERE ID = {self.choose}""").fetchall()
        if self.s == 'Название сорта':
            self.find = self.cur.execute(f"""SELECT * FROM coffee WHERE Sort = '{self.choose}'""").fetchall()
        elif self.s == 'Степень обжарки':
            self.find = self.cur.execute(f"""SELECT * FROM coffee WHERE degree_of_roasting = 
            '{self.choose}'""").fetchall()
        elif self.s == 'Молотый/в зёрнах':
            self.find = self.cur.execute(f"""SELECT * FROM coffee WHERE ground_in_grains =
             '{self.choose}'""").fetchall()
        elif self.s == 'Цена':
            self.find = self.cur.execute(f"""SELECT * FROM coffee WHERE price = {self.choose}""").fetchall()
        elif self.s == 'Объём упаковки':
            self.find = self.cur.execute(f"""SELECT * FROM coffee WHERE volume = {self.choose}""").fetchall()
        self.table.setColumnCount(6)
        self.table.setRowCount(0)
        for i, row in enumerate(self.find):
            self.table.setRowCount(self.table.rowCount() + 1)
            for j, elem in enumerate(row):
                self.table.setItem(i, j, QTableWidgetItem(str(elem)))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())