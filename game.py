import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt


class GAME(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Picture_Editor_Window")
        self.setGeometry(100, 100, 800, 800)
        self.setWindowIcon(QtGui.QIcon('Image_files\\tank_u.png'))

        self.image = QLabel(self)
        self.image.resize(100, 100)
        self.image.move(300, 300)

        self.xpos = 300
        self.ypos = 300

        self.Set_Picture('Image_files\\tank_u.png')
        

    def Set_Picture(self, filename):
        self.file_name = filename
        self.original_image, self.curr_image = QImage(self.file_name), QImage(self.file_name)
        self.pixmap = QPixmap(self.curr_image.copy())
        self.image.setPixmap(self.pixmap)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_W and self.ypos > 0:
            self.Set_Picture('Image_files\\tank_u.png')
            self.ypos -= 10
            self.image.move(self.xpos, self.ypos)

        elif event.key() == Qt.Key_S and self.ypos < 700:
            self.Set_Picture('Image_files\\tank_d.png')
            self.ypos += 10
            self.image.move(self.xpos, self.ypos)

        elif event.key() == Qt.Key_A and self.xpos > 0:
            self.Set_Picture('Image_files\\tank_l.png')
            self.xpos -= 10
            self.image.move(self.xpos, self.ypos)

        elif event.key() == Qt.Key_D and self.xpos < 700:
            self.Set_Picture('Image_files\\tank_r.png')
            self.xpos += 10
            self.image.move(self.xpos, self.ypos)


if __name__ == '__main__': 
    app = QApplication(sys.argv)
    ex = GAME()
    ex.show()
    sys.exit(app.exec_())
