import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QWidget
from Text_Editor_Window import Text_Editor
from Table_Editor import TableEditor
from Calculator_Window import Calculator
from SoundPad_Window import SoundPad
from Admin_Window import AdminWindow
from VideoPlayer_Window import VideoWindow
from Picture_Editor_Window import PictureEditor
from game import GAME
from PyQt5 import QtGui


class MainMenu_Window(QWidget):
    def __init__(self, *args):
        super().__init__()
        loadUi('Uic_files\Main_Menu_Window.ui', self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Main_Menu_Window")
        self.setWindowIcon(QtGui.QIcon('Image_files\\8_icon.png'))
        
        self.admin_button.clicked.connect(self.Admin_func)
        self.enter_button.clicked.connect(self.Enter_admin_version)
        
        self.password_label.hide()
        self.enter_password_line.hide()
        self.enter_button.hide()
        
        self.start_picture_editor.clicked.connect(self.Enter_Picture_Editor)
        self.start_game_button.clicked.connect(self.Enter_Game)
        self.start_soundpad_button.clicked.connect(self.Enter_soundpad)
        self.start_calculator_button.clicked.connect(self.Enter_calculator)
        self.start_table_editor_button.clicked.connect(self.Enter_table_editor)
        self.start_text_editor_button.clicked.connect(self.Enter_text_editor)
        self.start_video_player_button.clicked.connect(self.Enter_VideoPlayer)
        self.quit_button.clicked.connect(self.Quit_from_app)
        

    def Admin_func(self):
        self.password_label.show()
        self.enter_password_line.show()
        self.enter_button.show()

    def Enter_text_editor(self):
        self.text_editor_win = Text_Editor(self)
        self.text_editor_win.show()

    def Enter_calculator(self):
        self.calc_win = Calculator(self)
        self.calc_win.show()

    def Enter_table_editor(self):
        self.table_edit_win = TableEditor(self)
        self.table_edit_win.show()

    def Enter_soundpad(self):
        self.soundpad_win = SoundPad(self)
        self.soundpad_win.show()

    def Enter_VideoPlayer(self):
        self.videoplayer_win = VideoWindow(self)
        self.videoplayer_win.show()

    def Enter_Picture_Editor(self):
        self.pic_edit_win = PictureEditor(self)
        self.pic_edit_win.show()

    def Enter_Game(self):
        self.game_win = GAME(self)
        self.game_win.show()

    def Enter_admin_version(self):
        if self.enter_password_line.text() == 'Yandex_lyceum':
            self.admin_win = AdminWindow(self)
            self.admin_win.show()
        else:
            self.password_label.hide()
            self.enter_password_line.hide()
            self.enter_button.hide()
            

    def Quit_from_app(self):
        self.close()
        

if __name__ == '__main__': 
    app = QApplication(sys.argv)
    ex = MainMenu_Window()
    ex.show()
    sys.exit(app.exec_())
