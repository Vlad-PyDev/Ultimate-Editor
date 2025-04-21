import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit
from PyQt5 import QtGui


class Calculator(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Calculator")
        self.setWindowIcon(QtGui.QIcon('Image_files\\3_icon.png'))
        self.setGeometry(300, 300, 300, 300)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.result_display = QLineEdit()
        layout.addWidget(self.result_display)

        buttons_layout = QGridLayout()
        layout.addLayout(buttons_layout)

        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "=", "+"],
            ['Quit', 'C', 'CE', '%']
        ]
        row, col = 0, 0

        for button_row in buttons:
            for button_text in button_row:
                button = QPushButton(button_text)
                button.clicked.connect(self.Button_clicked)
                buttons_layout.addWidget(button, row, col)
                col += 1
            row += 1
            col = 0

    def Button_clicked(self):
        button = self.sender()
        button_text = button.text()
        if button_text == "=":
            try:
                self.result_display.setText(str(eval(self.result_display.text())))
            except Exception:
                self.result_display.setText("Error")
        elif button_text == 'C':
            self.result_display.setText('')
        elif button_text == 'CE':
            self.result_display.setText(self.result_display.text()[:-1])
        elif button_text == 'Quit':
            self.Quit_from_app()
        else:
            new_expression = self.result_display.text() + button_text
            self.result_display.setText(new_expression)

    def Quit_from_app(self):
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Calculator()
    ex.show()
