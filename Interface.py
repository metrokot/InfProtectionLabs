import sys
import time
from PyQt5 import uic

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QGridLayout, QMessageBox, QTextEdit
import filesmanager
'''
Autorisation
AddUser
passwordChange
Actions
UserList
'''

class Autorisation(QWidget):
    def __init__(self):
        super(Autorisation,self).__init__()
        self.initUI()
        
        
    
    def initUI(self):
        infoname = QLabel('Введите имя')
        infopass = QLabel('Введите пароль')
        self.name = QLineEdit()
        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.EchoMode.Password)

        btnOk = QPushButton('OK', self)
        btnOk.clicked.connect(self.getinfo)

        btnCancel = QPushButton('Cancel', self)
        btnCancel.clicked.connect(self.exit)

        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(infoname, 1, 0)
        grid.addWidget(self.name, 1, 1)

        grid.addWidget(infopass, 2, 0)
        grid.addWidget(self.password, 2, 1)

        grid.addWidget(btnOk, 3, 0)
        grid.addWidget(btnCancel, 3, 1)

        self.setLayout(grid)
        self.setGeometry(1000,500, 364, 328)
        self.setWindowTitle("Авторизация")
        
    
    def getinfo(self):
        name = self.name.text()
        passw = self.password.text()
        if name == '':
            self.msg = QMessageBox()
            self.msg.setText('Поле логин не должно быть пустым')
            self.msg.setIcon(QMessageBox.Warning)
            self.msg.show()

        else:
            user, error = filesmanager.checkUser(name, passw)
            if(user):
                if user.withoutpass == '1':
                    self.ps = PasswordChange(user)
                    self.ps.show()
                    
                else:
                    pass#переход на Actions
            else:
                self.msg = QMessageBox()
                self.msg.setText(error)
                self.msg.setIcon(QMessageBox.Warning)
                self.msg.show()
    def exit(self):
        self.close()

class PasswordChange(QWidget):
    def __init__(self, user):
        super(PasswordChange,self).__init__()
        self.user = user
        self.error = ''
        self.initUI()

    def initUI(self):
        infoname = QLabel('Имя пользователя')
        infolastpass = QLabel('Введите старый пароль')
        infonewpass = QLabel('Введите новый пароль')
        infoconfirmpass = QLabel('Введите новый пароль')
        infoerror = QLabel(self.error)
        name = QLabel(self.user.login)
        self.lastpass = QLineEdit()
        self.newpass = QLineEdit()
        self.confirmpass = QLineEdit()
        self.lastpass.setEchoMode(QLineEdit.EchoMode.Password)
        self.newpass.setEchoMode(QLineEdit.EchoMode.Password)
        self.confirmpass.setEchoMode(QLineEdit.EchoMode.Password)

        btnOk = QPushButton('OK', self)
        btnOk.clicked.connect(self.trychange)

        btnCancel = QPushButton('Cancel', self)
        btnCancel.clicked.connect(self.exit)

        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(infoname, 1, 0)
        grid.addWidget(name, 1, 1)

        grid.addWidget(infolastpass, 2, 0)
        grid.addWidget(self.lastpass, 2, 1)

        grid.addWidget(infonewpass, 3, 0)
        grid.addWidget(self.newpass, 3, 1)

        grid.addWidget(infoconfirmpass, 4, 0)
        grid.addWidget(self.confirmpass, 4, 1)

        grid.addWidget(btnOk, 5, 0)
        grid.addWidget(btnCancel, 5, 1)

        grid.addWidget(infoerror, 6,0)

        self.setLayout(grid)
        self.setGeometry(1000,500, 400, 370)
        self.setWindowTitle("Авторизация")


    def trychange(self):
        lastpass = self.lastpass.text()
        newpass =  self.newpass.text()
        confirmpass = self. confirmpass.text()
        self.msg = QMessageBox()
        self.msg.setText('Пароль успешно установлен')
        if not (error:=filesmanager.setpassword(self.user, lastpass, newpass, confirmpass)):
            self.msg.show()
            time.sleep(5)
            exit()
        else:
            self.msg.setText(error)
            self.msg.show()
        

    def exit(self):
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Autorisation()
    ex.show()
    sys.exit(app.exec_())