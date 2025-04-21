import sys
from PyQt5 import QtCore, QtMultimedia
from PyQt5.uic import loadUi
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget


class AdminWindow(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI()

    def initUI(self):
        loadUi('Uic_files\Admin_Window.ui', self)
        self.setWindowTitle("Admin_Window")
        self.setWindowIcon(QtGui.QIcon('Image_files\\7_icon.png'))

        self.dowload_users_button.clicked.connect(self.dowload_users_db)
        self.dowload_reviews_button.clicked.connect(self.dowload_reviews_db)
        self.quit_button.clicked.connect(self.Quit_from_app)

    def dowload_users_db(self):
        f = open('Text_Data_Base _files\\USERS_DATA_BASE.txt', 'r')
        self.users_list.setPlainText('\n'.join([i.strip() for i in f.readlines()]))
        f.close()

    def dowload_reviews_db(self):
        f = open('Text_Data_Base _files\\REVIEW_DATA_BASE.txt', 'r')
        self.review_list.setPlainText('\n'.join([i.strip() for i in f.readlines()]))
        f.close()

    def Quit_from_app(self):
        self.close()


if __name__ == '__main__': 
    app = QApplication(sys.argv)
    ex = AdminWindow()
    ex.show()
    sys.exit(app.exec_())
