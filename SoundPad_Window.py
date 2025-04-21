import sys
from PyQt5 import QtCore, QtMultimedia
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia
from PyQt5 import QtGui
import os


class SoundPad(QWidget):
    def __init__(self, *args):
        super().__init__()
        loadUi('Uic_files\SoundPad_Window.ui', self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("SoundPad_Window")
        self.setWindowIcon(QtGui.QIcon('Image_files\\5_icon.png'))
        
        self.playBtn.clicked.connect(self.Play_sound)
        self.loadBtn.clicked.connect(self.Load_sound)
        self.stopBtn.clicked.connect(self.Stop_sound)
        self.quit_button.clicked.connect(self.Quit_from_app)

    def Play_sound(self):
        try:
            item = self.listWidget.currentItem()

            if item:
                file_name = os.path.join(self.dir, item.text())
                content = QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile(file_name))

                self.mediaPlayer = QtMultimedia.QMediaPlayer()
                self.mediaPlayer.setMedia(content)
                self.mediaPlayer.play()
            else:
                self.listWidget.setCurrentRow(0)
                self.play()
        except:
            pass

    def Stop_sound(self):
        try:
            self.mediaPlayer.stop()
        except:
            pass

    def Load_sound(self):
        self.listWidget.clear()

        dir = QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory")

        if dir:
            for file_name in os.listdir(dir):
                if file_name.endswith(".mp3"):
                    self.listWidget.addItem(os.path.join(file_name))
            self.dir = dir

    def Quit_from_app(self):
        self.close()


if __name__ == '__main__': 
    app = QApplication(sys.argv)
    ex = SoundPad()
    ex.show()
    sys.exit(app.exec_())
