from PyQt6.QtWidgets import *

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.number = 0
        self.initUI()

    def initUI(self):
        self.resize(700, 400)
        self.setWindowTitle("Кликер")
        self.setFixedSize(self.width(), self.height())
        self.batton = QPushButton('Жми')
        self.batton.clicked.connect(self.number2)
        self.check = QLabel(f"Счетчик: {self.number}")
        main_vl = QVBoxLayout()
        main_vl.addStretch()
        main_vl.addWidget(self.batton)
        main_vl.addWidget(self.check)
        main_vl.addStretch()
        self.setLayout(main_vl)

    def number2(self):
        self.number += 1
        self.check.setText(f"Счетчик: {self.number}")

def main():
    app = QApplication([])
    win = MainWin()
    win.show()
    app.exec()

if __name__ == "__main__":
    main()