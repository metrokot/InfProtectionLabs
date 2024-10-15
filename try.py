import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget

class App(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.window1 = QMainWindow()
        uic.loadUi('autorisation.ui', self.window1)
        self.window1.butt_ok.clicked.connect(self.check_pass)

    def check_pass(self):
        mode = self.filework()
        if mode:
            self.actions(mode)
    def filework(self):
        f = open("users.txt", 'r')
        for line in f:
            check= line.strip().split()
            if self.login.text() == check[0]:
                if self.password.text() == check[1]:
                    return check[2]
                else:
                    pass
        return False
    def actions(self, mode):
        self.window2 = QMainWindow()
        uic.loadUi('actions.ui', self.window2)
        self.window2.show()
        if mode != 'admin':
            self.window2.add_user.hide()
            self.window2.users_list.hide()
        self.password_change.clicked.connect(self.passwordChange)
        self.add_user.clicked.connect(self.check_pass)
        self.users_list.clicked.connect(self.check_pass)
        self.exit.clicked.connect(self.exitActions)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = App()
    win.show()
    sys.exit(app.exec())