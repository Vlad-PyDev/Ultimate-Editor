import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTextEdit, QVBoxLayout, QWidget
from PyQt5.uic import loadUi
from PyQt5 import QtGui
from Main_Menu_Window import MainMenu_Window


class LoginWindow(QWidget):
    def __init__(self, *args):
        super().__init__()
        loadUi('Uic_files\Login_Window.ui', self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Login_Window")
        self.setWindowIcon(QtGui.QIcon('Image_files\\4_icon.png'))

        self.quit_button.clicked.connect(self.Quit_from_app)
        self.login_button.clicked.connect(self.Log_user)
        self.error_line.hide()

    def Log_user(self):
        f = open('Text_Data_Base _files\\LOGIN_DATA_BASE.txt', 'r')
        sp = [i.strip().split() for i in f.readlines()]
        f.close()
        for i in sp:
            try:
                if i[0] == self.username_line.text():
                    if  i[1] == self.password_line.text():
                        self.close()
                        self.main_menu_window = MainMenu_Window(self)
                        self.main_menu_window.show()
                        break
            except:
                pass
        else:
            self.error_line.show()
            self.username_line.clear()
            self.password_line.clear()
        
 
    def Quit_from_app(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    start_window = LoginWindow()
    start_window.show()
