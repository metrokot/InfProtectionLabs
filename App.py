import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('autorisation.ui', self)
        self.butt_ok.clicked.connect(self.check_pass)
    def check_pass(self):
        mode = self.filework()
        self.Actions()

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
class AddUser(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('AddUser.ui', self)
class PasswordChange(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('passwordChange.ui', self)
class UserList(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UserList.ui', self)

class Actions(QWidget):
    def __init__(self):
        super().__init__()
        self.window2 = QWidget()
        uic.loadUi('action.ui', self.window2)
        self.window2.show()


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
    ex = App()
    ex.show()
    sys.exit(app.exec_())
