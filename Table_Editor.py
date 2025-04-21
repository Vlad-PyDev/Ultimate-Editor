import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtGui


class TableEditor(QMainWindow):
    def __init__(self, *args):
        super().__init__()
        uic.loadUi('Uic_files\\Table_Editor.ui', self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Table_Editor_Window")
        self.setWindowIcon(QtGui.QIcon('Image_files\\6_icon.png'))
        self.connection = sqlite3.connect("DataBase_files\\DataBase.sqlite")
        #self.append_button.clicked.connect(self.Append_to_db)
        self.delete_button.clicked.connect(self.Delete_from_db)
        self.exec_button.clicked.connect(self.Select_data)
        self.quit_button.clicked.connect(self.Quit_from_app)
        self.Select_data()

    def Select_data(self):
        try:
            self.connection.commit()
            self.connection.close()
            self.connection = sqlite3.connect(self.Filename_text.text())
            query = self.textEdit.toPlainText()
            res = self.connection.cursor().execute(query).fetchall()
            self.tableWidget.setColumnCount(5)
            self.tableWidget.setRowCount(0)
            for i, row in enumerate(res):
                self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
                for j, elem in enumerate(row):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(elem)))
        except:
            pass

#    def Append_to_db(self):
 #       try:
 #           sp = tuple([i for i in self.append_line.text().split()])
 #           print(sp)
 #           self.connection.commit()
  #          self.connection.close()
   #         self.connection = sqlite3.connect(self.Filename_text.text())
   #         res = self.connection.cursor().execute(f"INSERT INTO {self.table_name_line.text()} VALUES {sp}")
   #         res1 = self.connection.cursor().execute(f"SELECT * from {self.table_name_line.text()}").fetchall()
   #         self.tableWidget.setColumnCount(5)
   #         self.tableWidget.setRowCount(0)
   #         for i, row in enumerate(res1):
   #             self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
   #             for j, elem in enumerate(row):
   #                 self.tableWidget.setItem(i, j, QTableWidgetItem(str(elem)))
   #     except:
    #        pass

    def Delete_from_db(self):
        try:
            self.connection.commit()
            self.connection.close()
            self.connection = sqlite3.connect(self.Filename_text.text())
            res = self.connection.cursor().execute(f"DELETE FROM {self.table_name_line.text()} where id = {int(self.id_line.text())}")
            res1 = self.connection.cursor().execute(f"SELECT * from {self.table_name_line.text()}").fetchall()
            self.tableWidget.setColumnCount(5)
            self.tableWidget.setRowCount(0)
            for i, row in enumerate(res1):
                self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
                for j, elem in enumerate(row):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(elem)))
        except:
            pass
        

    def Quit_from_app(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TableEditor()
    ex.show()
    sys.exit(app.exec())
