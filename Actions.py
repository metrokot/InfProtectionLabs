import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget

class Actions(QWidget):
    def __init__(self):
        super(Actions, self).__init__()
        uic.loadUi('action.ui', self)
        if 1 != 'admin':
            self.add_user.hide()
            self.users_list.hide()
        self.password_change.clicked.connect(self.passwordChange)
        self.add_user.clicked.connect(self.check_pass)
        self.users_list.clicked.connect(self.check_pass)
        self.exit.clicked.connect(self.exitActions)
    def passwordChange(self):
        pass
    def addUser(self):
        pass
    def usersList(self):
        pass
    def exitActions(self):
        self.hide()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Actions()
    ex.show()
    sys.exit(app.exec_())