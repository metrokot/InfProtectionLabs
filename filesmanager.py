class User():
    def __init__(self, params):
        self.login = params[0]
        self.password = params[1]
        self.mode = params[2]
        self.ban = params[3]
        self.withoutpass = params[4]
    def get(self):
        return f'{"|".join((self.login, self.password, self.mode, self.ban, self.withoutpass))}'+'\n'

def checkUser(login, password):
    f = open("users.txt", 'r')
    f1 = open('users2.txt','w')
    user, error = 0, ''
    for line in f:
        user1 = User(line.strip().split('|'))
        if login == user1.login:
            if int(user1.ban):
                error = "Вы заблокированы"
            if password == user1.password:
                user = user1
            else:
                error = "Неверный пароль"
        f1.write(user1.get())
    f1.close()
    f.close()
    filechanger()
    return user, error


def setpassword(user, lastpass, newpass, confirmpass):
    error = 0
    if lastpass != '':
        error = 'Неверный предыдуший пароль'
    if newpass != confirmpass:
        error = 'Неверное подтверждение пароля'
    if not error:
        with open('users.txt', 'r') as f:
            old_data = f.read()
        new_data = old_data.replace(f'{user.login}|{user.password}', f'{user.login}|{newpass}')
        with open('users.txt', 'w') as f:
            f.write(new_data)
    return error

    
def menu(user):
    print('1. Изменение пароля')
    if(user.admin):
        print('2. Добавление пользователя')
        print('3. Список пользователей')
    print('4. Выход')
    i = int(input("Введите интересующий режим "))
    if i==1:
        passChange(user)
    elif i==2 and user.admin:
        newUser()
    elif i==3 and user.admin:
        newUser()
    elif i==4:
        return True
    else:
        print("Неверный ввод")
    menu(user)
def passChange(user):
    lastpass = input("Введите старый пароль: ")
    if lastpass != user.password:
        print('Неверный предыдуший пароль')
        if not contin():
            return False
        else:
            return passChange(user)
    newpass = input("Введите новый пароль: ")
    with open('users.txt', 'r') as f:
        old_data = f.read()
    new_data = old_data.replace(f'{user.login}|{user.password}', f'{user.login}|{newpass}')
    with open('users.txt', 'w') as f:
        f.write(new_data)
    return True

def contin():
    mode = int(input(
'''Если хотите продолжить введите   1
Если хотите выйти введите   0
    '''))
    if mode ==1:
        return True
    elif mode == 0:
        return False
    else:
        print("Неверный ввод")
        return contin()
def newUser():
    login = input("Введите имя нового пользователя: ")
    f = open("users.txt", 'a')
    f.write(f'{login}||user|0|0' + '\n')
    return True
def UserList(skip=0):
    f = open("users.txt", 'r')
    f1 = open('users2.txt','w')
    for line in f:
        check = line.strip().split('|')
        if not skip:
            getUserParams(check)
            edit = int(input('''Для изменения данных введите 1 
Для показа следующего пользователя введите 2
Для выхода нажмите 0'''))
        else:
            edit=2
        if edit:
            if edit==1:
                check[0] = input("Введите новый логин")
                check[1] = input("Введите новый пароль")
                check[3] = input("Введите состояние блокировки")
                check[4] = input("Введите состояние вход без пароля")
            f1.write(f'{"|".join(check)}'+'\n')
        else:
            skip = 1
    f.close()
    f1.close()
def filechanger():
    f = open("users.txt", 'w')
    f1 = open('users2.txt', 'r')
    content = f1.read()
    f.write(content)
    f.close()
    f1.close()
def getUserParams(list):
    print(
f'''
Имя пользователя: {list[0]}
Пароль: {list[1]}
Блокировка: {list[3]}
Вход без пароля: {list[4]}
''')