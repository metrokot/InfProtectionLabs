import sys
import time
from PyQt5 import uic

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QGridLayout, QMessageBox, QCheckBox
import filesmanager
from PyQt5.QtCore import Qt
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
                    self.pss = PasswordChange(user)
                    self.pss.show()
                    
                else:
                    if user.mode == 'admin':
                        self.act = AdminActions(user)
                        self.act.show()
                    if user.mode == 'user':
                        self.act = UserActions(user)
                        self.act.show()
                self.password.setText('')
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
        confirmpass = self.confirmpass.text()
        self.msg = QMessageBox()
        self.msg.setText('Пароль успешно установлен')
        error=filesmanager.setpassword(self.user, lastpass, newpass, confirmpass)
        if not error:
            self.msg.show()
            self.lastpass.setText('')
            self.newpass.setText('')
            self.confirmpass.setText('')
            #если в этот момент нужно выходить из акка
            #exit()
        else:
            self.msg.setText(error)
            self.msg.show()
        

    def exit(self):
        self.close()

class AdminActions(QWidget):
    def __init__(self, user):
        super(AdminActions,self).__init__()
        self.user = user
        self.initUI()
    
    def initUI(self):
        btnPassCange = QPushButton('Смена пароля', self)
        btnPassCange.clicked.connect(self.passChange)

        btnAdd = QPushButton('Добавление пользователей', self)
        btnAdd.clicked.connect(self.add)

        btnAdminca = QPushButton('Администрирование', self)
        btnAdminca.clicked.connect(self.adminca)

        btnExit = QPushButton('Выйти', self)
        btnExit.clicked.connect(self.exit)

        grid = QGridLayout()
        grid.setSpacing(10)
        
        grid.addWidget(btnPassCange, 1, 0)
        grid.addWidget(btnAdd, 2, 0)
        grid.addWidget(btnAdminca, 3, 0)  
        grid.addWidget(btnExit, 4, 0)
        
        self.setLayout(grid)
        self.setGeometry(1000,500, 200, 237)
        self.setWindowTitle("Действия")
        

    def passChange(self):
        self.ps = PasswordChange(self.user)
        self.ps.show()
    
    def add(self):
        self.ad = AddUser()
        self.ad.show()
    
    def adminca(self):
        self.adm = Adminca()
        self.adm.show()
    
    def exit(self):
        self.close()

class UserActions(QWidget):
    def __init__(self, user):
        super(UserActions,self).__init__()
        self.user = user
        self.initUI()
    
    def initUI(self):
        btnPassCange = QPushButton('Смена пароля', self)
        btnPassCange.clicked.connect(self.passChange)

        btnExit = QPushButton('Выйти', self)
        btnExit.clicked.connect(self.exit)

        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(btnPassCange, 1, 0)
        grid.addWidget(btnExit, 2, 0)
        
        self.setLayout(grid)
        self.setGeometry(1000,500, 200, 237)
        self.setWindowTitle("Действия")
        

    def passChange(self):
        self.ps = PasswordChange(self.user)
        self.ps.show()
    
    def exit(self):
        self.close()


class AddUser(QWidget):
    def __init__(self):
        super(AddUser,self).__init__()
        self.initUI()
    def initUI(self):
        infoname = QLabel('Введите имя')
        self.name = QLineEdit()

        btnOk = QPushButton('OK', self)
        btnOk.clicked.connect(self.addUser)

        btnCancel = QPushButton('Cancel', self)
        btnCancel.clicked.connect(self.exit)

        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(infoname, 1, 0)
        grid.addWidget(self.name, 1, 1)

        grid.addWidget(btnOk, 2, 0)
        grid.addWidget(btnCancel, 2, 1)

        self.setLayout(grid)
        self.setGeometry(1000,500, 362, 195)
        self.setWindowTitle("Добавление")


    def addUser(self):
        login = self.name.text()
        filesmanager.newUser(login)
    def exit(self):
        self.close()

class Adminca(QWidget):
    def __init__(self):
        super(Adminca,self).__init__()
        self.userList = filesmanager.UserList()
        self.newuserfromlist()
        f = open("users2.txt", 'w')
        f.close()
        self.initUI()
        self.saving = False
    def newuserfromlist(self):
        userr = self.userList.pop(0)
        self.user = filesmanager.User([userr.login, userr.password, userr.mode, userr.ban, userr.withoutpass])
        self.newuser = filesmanager.User([userr.login, userr.password, userr.mode, userr.ban, userr.withoutpass])
        

    def initUI(self):
        infoname = QLabel('Имя пользователя')
        infoban = QLabel('Блокировка')
        infowithoutpass = QLabel('Вход без пароля')
        self.name = QLabel(self.newuser.login)
        self.ban = QCheckBox(self)
        self.withoutpass = QCheckBox(self)

        if self.newuser.ban == '1':
            self.ban.setChecked(True)
        if self.newuser.withoutpass == '1':
            self.withoutpass.setChecked(True)
        
        self.ban.stateChanged.connect(self.changeBan)
        self.withoutpass.stateChanged.connect(self.changewithoutpass)

        btnNext = QPushButton('Следующий', self)
        btnNext.clicked.connect(self.next)

        btnSave = QPushButton('Сохранить', self)
        btnSave.clicked.connect(self.save)

        btnCancel = QPushButton('Выйти', self)
        btnCancel.clicked.connect(self.exit)

        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(infoname, 1, 0)
        grid.addWidget(self.name, 1, 1)

        grid.addWidget(infoban, 2, 0)
        grid.addWidget(self.ban, 2, 1)

        grid.addWidget(infowithoutpass, 3, 0)
        grid.addWidget(self.withoutpass, 3, 1)

        grid.addWidget(btnNext, 4, 0)
        grid.addWidget(btnSave, 4, 1)

        grid.addWidget(btnCancel, 5, 0)

        self.setLayout(grid)
        self.setGeometry(1000,500, 400, 370)
        self.setWindowTitle("Администрирование")
    
    

    def changeBan(self, state):

        if state == Qt.Checked:
            self.newuser.ban = '1'
        else:
            self.newuser.ban = '0'
    
    def changewithoutpass(self, state):

        if state == Qt.Checked:
            self.newuser.withoutpass = '1'
        else:
            self.newuser.withoutpass = '0'

    def save(self):
        self.user = self.newuser
        self.loadintofile(self.user)
        self.saving=True

    def next(self):
        if not self.saving:
            self.loadintofile(self.user)
            self.saving=True
        if self.userList != []:
            self.newuserfromlist()
            if self.newuser.ban == '1':
                self.ban.setChecked(True)
            else:
                self.ban.setChecked(False)
            if self.newuser.withoutpass == '1':
                self.withoutpass.setChecked(True)
            else:
                self.withoutpass.setChecked(False)
            self.name.setText(self.newuser.login)
            self.saving = False
        else:
            self.msgg = QMessageBox()
            self.msgg.setText('Список закончился')
            self.msgg.show()
        

        
    def loadintofile(self, uuser):
        f = open("users2.txt", 'a')
        f.write(str(uuser.get()))
        f.close()

    def exit(self):#следующий и выход должны по разному обрабатываться
        if not self.saving:
            self.loadintofile(self.user)
        for elem in self.userList:
            self.loadintofile(elem)
        filesmanager.filechanger()
        self.close()


class KeyPass(QWidget):
    def __init__(self):
        super(KeyPass,self).__init__()
        self.initUI()
        
        
    def initUI(self):
        info = QLabel('Введите ключевую фразу')
        self.key = QLineEdit()
        self.key.setEchoMode(QLineEdit.EchoMode.Password)

        btnOk = QPushButton('Check', self)
        btnOk.clicked.connect(self.getinfo)

        btnCancel = QPushButton('Cancel', self)
        btnCancel.clicked.connect(self.exit)

        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(info, 1, 0)
        grid.addWidget(self.key, 1, 1)
        grid.addWidget(btnOk, 2, 0)
        grid.addWidget(btnCancel, 2, 1)
        self.setLayout(grid)
        self.setGeometry(1000,500, 200, 200)
        self.setWindowTitle("Проверка доступа")

    def getinfo(self):
        txt = self.key.text()
        if filesmanager.keypass(txt):
            self.ex = Autorisation()
            self.hide()
            self.ex.show()
            
        else:
            self.msggg = QMessageBox()
            self.msggg.setText('Не верная фраза')
            self.msggg.show()
    def closeEvent(self, event):
        event.ignore()
    def exit(self):
        exit()
if __name__ == '__main__':
    filesmanager.predobrabot()
    
    app = QApplication(sys.argv)
    check = KeyPass()
    check.show()
    while app.exec_()!=1:
        pass
    print(1)
    filesmanager.shifrSHA()
    sys.exit(1)
