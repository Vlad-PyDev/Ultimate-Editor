import sys
import os
from PyQt5.uic import loadUi
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QPushButton, QPlainTextEdit, QLineEdit, QWidget


class Text_Editor(QWidget):
    def __init__(self, *args):
        super().__init__()
        loadUi('Uic_files\Text_Editor_Window.ui', self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Text_Editor_Window")
        self.setWindowIcon(QtGui.QIcon('Image_files\\2_icon.png'))
        
        self.create_button.clicked.connect(self.New_file)
        self.save_button.clicked.connect(self.Save_file)
        self.open_button.clicked.connect(self.Open_file)
        self.delete_button.clicked.connect(self.Delete_file)
        self.quit_button.clicked.connect(self.Quit_from_app)

    def New_file(self):
        self.filename_edit.clear()
        self.textEdit.clear()

    def Save_file(self):
        if self.filename_edit.text():
            f = open(self.filename_edit.text(), 'w')
            f.write(self.textEdit.toPlainText())
            f.close()

    def Delete_file(self):
        try:
            os.remove(self.filename_edit.text())
        except FileNotFoundError:
            pass

    def Open_file(self):
        try:
            with open(self.filename_edit.text(), 'r') as f:
                a = f.read()
                self.textEdit.setText(a)
                f.close()
        except FileNotFoundError:
            pass

    def Quit_from_app(self):
        self.close()


if __name__ == '__main__': 
    app = QApplication(sys.argv)
    ex = Text_Editor()
    ex.show()
    sys.exit(app.exec_())
