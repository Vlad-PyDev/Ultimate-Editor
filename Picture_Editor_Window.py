import sys
import os
from PyQt5.uic import loadUi
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QImage, QTransform, QPixmap, qRgb
from PyQt5.QtWidgets import QFileDialog
import shutil
from itertools import product
from copy import deepcopy


class PictureEditor(QWidget):
    def __init__(self, *args):
        super().__init__()
        loadUi('Uic_files\\Picture_Editor_Window.ui', self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Picture_Editor_Window")
        self.setWindowIcon(QtGui.QIcon('Image_files\\1_icon.png'))
        
        self.quit_button.clicked.connect(self.Quit_from_app)
        self.select_button.clicked.connect(self.Select_file)
        self.turn_right_button.clicked.connect(self.Turn_right_picture)
        self.turn_left_button.clicked.connect(self.Turn_left_picture)
        self.save_button.clicked.connect(self.Save_as_new_picture)

        self.angle = 0
        self.color = "C"
        self.pic_num = 1

        self.set_red_color_button.clicked.connect(self.change_color)
        self.set_blue_color_button.clicked.connect(self.change_color)
        self.set_green_color_button.clicked.connect(self.change_color)
        self.reset_button.clicked.connect(self.change_color)

    def change_color(self):
        st = self.sender().text().split()
        self.color = st[-1][0].upper()
        self.show_image()
    
    def Select_file(self):
        try:
            self.file_name = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')[0]
            self.original_image, self.curr_image = QImage(self.file_name), QImage(self.file_name)
            self.pixmap = QPixmap(self.curr_image.copy())
            self.image.setPixmap(self.pixmap)
        except FileNotFound:
            pass

    def Turn_right_picture(self):
        try:
            self.angle = (self.angle + 90) % 360
            self.show_image()
        except:
            pass

    def Turn_left_picture(self):
        try:
            self.angle = (self.angle - 90) % 360
            self.show_image()
        except:
            pass

    def show_image(self):
        try:
            self.curr_image = self.original_image.copy()
            self.pixmap = QPixmap(self.curr_image.copy())
     
            if self.color != "C":
                x, y = self.pixmap.size().width(), self.pixmap.size().height()
     
                for i, j in product(range(x), range(y)):
                    r, g, b, a = self.curr_image.pixelColor(i, j).getRgb()
                    r, g, b = (self.color == "R") * r, (self.color == "G") * g, (self.color == "B") * b
                    self.curr_image.setPixel(i, j, qRgb(r, g, b))
     
            self.curr_image = self.curr_image.transformed(QTransform().rotate(self.angle))
            self.pixmap = QPixmap(self.curr_image.copy())
            self.image.setPixmap(self.pixmap)
        except:
            pass

    def Save_as_new_picture(self):
        try:
            self.pixmap.save(f'Result_image_files\\Image_{self.pic_num}.png', 'png')
            self.pic_num += 1
        except:
            pass
         
    def Quit_from_app(self):
        self.close()


if __name__ == '__main__': 
    app = QApplication(sys.argv)
    ex = PictureEditor()
    ex.show()
    sys.exit(app.exec_())
