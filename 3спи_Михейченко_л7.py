from PyQt6.QtWidgets import *


class AuthWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(300, 450)
        self.setWindowTitle("Авторизация")

        self.login_edit = QLineEdit()
        self.login_edit.setPlaceholderText("Логин")
        self.password_edit = QLineEdit()
        self.password_edit.setPlaceholderText("Пароль")
        self.password_edit.setEchoMode(QLineEdit.EchoMode.Password)
        self.login_bt = QPushButton("Вход в систему")
        self.login_bt.clicked.connect(self.check_auth)

        main_vl = QVBoxLayout()
        main_vl.addWidget(self.login_edit)
        main_vl.addWidget(self.password_edit)
        main_vl.addWidget(self.login_bt)
        self.setLayout(main_vl)

    def check_auth(self):
        login = self.login_edit.text()
        password = self.password_edit.text()
        if login == "ГООЛ" and password == "123":
            QMessageBox.information(self, "Окно", "      Вход в систему      ")
        else:
            QMessageBox.warning(self, "Окно", "      Авторизация пользователя ошибка      ")


def main():
    app = QApplication([])
    win = AuthWin()
    win.show()
    app.exec()


if __name__ == "__main__":
    main()