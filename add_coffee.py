from PyQt5 import uic
from PyQt5.QtWidgets import *
import sqlite3
import sys


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.connection = sqlite3.connect('capuccino.sqlite')
        self.cur = self.connection.cursor()
        self.add.clicked.connect(self.add_coffee)
        self.table.setColumnCount(6)
        self.delete_2.clicked.connect(self.del_coffee)
        self.show_2.clicked.connect(self.show_data)
        self.change.clicked.connect(self.set_data)

    def set_data(self):
        self.val = int(self.spin_del.value())
        self.sort_name = self.sort.text()
        self.roast_name = self.degree.text()
        self.beans = self.ground.text()
        self.price_name = self.price.text()
        self.volume_name = self.volume.text()
        self.result = self.cur.execute(f"""UPDATE coffee SET (ID, sort, degree_of_roasting, ground_in_grains, 
        price, volume) = ({self.id}, '{self.sort_name}', '{self.roast_name}', '{self.beans}', 
        {int(self.price_name)},{int(self.volume_name)}) WHERE ID = {self.val}""")
        self.show_data()

    def add_coffee(self):
        self.ids = self.cur.execute("""SELECT ID FROM coffee""").fetchall()
        self.id = int(self.ids[-1][0])
        self.sort_name = self.sort.text()
        self.roast_name = self.degree.text()
        self.beans = self.ground.text()
        self.price_name = self.price.text()
        self.volume_name = self.volume.text()
        self.id += 1
        self.result = self.cur.execute(f"""INSERT INTO coffee (ID, sort, degree_of_roasting, ground_in_grains, 
        price, volume) VALUES ({self.id}, '{self.sort_name}', '{self.roast_name}', '{self.beans}', 
        {int(self.price_name)},{int(self.volume_name)})""")
        self.connection.commit()
        print(self.result)
        self.show_data()
    def del_coffee(self):
        self.val = int(self.spin_del.value())
        self.r = self.cur.execute(f"""SELECT * FROM coffee WHERE ID = {self.val}""").fetchall()
        self.r = self.cur.execute(f"""DELETE FROM coffee WHERE ID = {self.val}""")
        self.connection.commit()
        self.show_data()

    def show_data(self):
        self.table.setRowCount(0)
        self.result = self.cur.execute("""SELECT * FROM coffee""")
        for i, row in enumerate(self.result):
            self.table.setRowCount(self.table.rowCount() + 1)
            for j, elem in enumerate(row):
                self.table.setItem(i, j, QTableWidgetItem(str(elem)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())