import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTextEdit, QVBoxLayout, QWidget
from PyQt5.uic import loadUi
import socket
from PyQt5 import QtGui
from Main_Menu_Window import MainMenu_Window
from datetime import datetime as dt
from Login_Window import LoginWindow


class Registration_Window(QWidget):
    def __init__(self, *args):
        super().__init__()
        loadUi('Uic_files\Registration_Window.ui', self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Registration_Window")
        self.setWindowIcon(QtGui.QIcon('Image_files\\4_icon.png'))

        self.quit_button.clicked.connect(self.Quit_from_app)
        self.reg_button.clicked.connect(self.Reg_user)
        self.login_button.clicked.connect(self.Enter_Login_Window)

    def Reg_user(self):
        f = open('Text_Data_Base _files\\USERS_DATA_BASE.txt', 'a')
        f1 = open('Text_Data_Base _files\\LOGIN_DATA_BASE.txt', 'a')
        
        print('------------------------------------', file=f)
        print(f'имя пользователя - {self.username_line.text()}', file=f)
        print(f'возраст пользователя- {self.age_line.text()}', file=f)
        print(f'дата рождения пользователя - {self.date_line.text()}', file=f)
        print(f'почта пользователя - {self.email_line.text()}', file=f)
        print(f'пароль пользователя - {self.password_line.text()}', file=f)
        print (f'ip адрес пользователя - {socket.gethostbyname("www.goole.com")}', file=f)
        print(f'дата регистрации - {dt.now()}', file=f)
        print('------------------------------------', file=f)
        
        print(f'{self.username_line.text()} {self.password_line.text()}', file=f1)

        self.main_menu_window = MainMenu_Window(self)
        self.main_menu_window.show()
        
        f.close()
        f1.close()
        self.close()

    def Enter_Login_Window(self):
        self.login_window = LoginWindow(self)
        self.login_window.show()
        self.close()
 
    def Quit_from_app(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    start_window = Registration_Window()
    start_window.show()
    sys.exit(app.exec_())
