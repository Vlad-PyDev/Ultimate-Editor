import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,  QWidget
from PyQt5 import QtGui
from PyQt5.uic import loadUi
from Registration_Window import Registration_Window
from datetime import datetime as dt

class Start_Window(QWidget):
    def __init__(self, *args):
        super().__init__()
        loadUi('Uic_files\Start_Window.ui', self)
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Start_Window")
        self.setWindowIcon(QtGui.QIcon('Image_files\\10_icon.png'))
        
        self.start_button.clicked.connect(self.Start_application)
        self.quit_button.clicked.connect(self.Quit_from_app)
        self.otziv_button.clicked.connect(self.Review_for_application)
        self.save_button.clicked.connect(self.Save_review)

        self.ask_line.hide()
        self.save_button.hide()
        self.Review_Text_Edit.hide()

    def Start_application(self):
        self.close()
        self.second_form = Registration_Window(self)
        self.second_form.show()

    def Review_for_application(self):
        self.ask_line.show()
        self.save_button.show()
        self.Review_Text_Edit.show()

    def Save_review(self):
        f = open('Text_Data_Base _files\REVIEW_DATA_BASE.txt', 'a')
        print('------------------------------------------------', file=f)
        print(f'{self.Review_Text_Edit.toPlainText()}', file=f)
        print(f'время написания отзыва - {dt.now()}', file=f)
        print('------------------------------------------------', file=f)
        f.close()

    def Quit_from_app(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    start_window = Start_Window()
    start_window.show()
    sys.exit(app.exec_())
