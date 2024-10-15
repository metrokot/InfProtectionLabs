#admin = 1
#user = 0
class User:
    def __init__(self, login, password, admin):
        self.login = login
        self.password = password
        if admin == 'admin':
            self.admin = 1
        else: self.admin = 0

def auto():
    name = input("Введите логин: ")
    password = input("Введите пароль: ")
    mode = checkUser(name, password)
    if(mode):
        menu(User(name,password, mode))
def checkUser(login, password):
    f = open("users.txt", 'r')
    f1 = open('users2.txt','w')
    mode = 0
    for line in f:
        check = line.strip().split('|')
        if login == check[0]:
            if int(check[3]):
                print("Вы заблокированы")
            if int(check[4]):
                check[1] = setpassword()
                check[4] = 0
                password = input("Введите пароль: ")
            if password == check[1]:
                mode = check[2]
            else:
                print("Неверный пароль")
        f1.write(f'{"|".join(check)}'+'\n')
    f1.close()
    f.close()
    filechanger()
    return mode
def setpassword():
    lastpass = input("Введите новый пароль: ")
    newpass = input("Установите новый пароль: ")
    if lastpass != newpass:
        print('Неверный предыдуший пароль')
        if not contin():
            return False
        else:
            newpass = setpassword()
    return newpass

    with open('users.txt', 'r') as f:
        old_data = f.read()
    new_data = old_data.replace(f'{user.login}|{user.password}', f'{user.login}|{newpass}')
    with open('users.txt', 'w') as f:
        f.write(new_data)
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
        UserList()
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
Для выхода нажмите 0
'''))
        else:
            edit=2
        if edit:
            if edit==1:
                check[0] = input("Введите новый логин: ")
                check[1] = input("Введите новый пароль: ")
                check[3] = input("Введите состояние блокировки: ")
                check[4] = input("Введите состояние вход без пароля: ")
            f1.write(f'{"|".join(check)}'+'\n')
        else:
            skip = 1
            f1.write(f'{"|".join(check)}' + '\n')
    f.close()
    f1.close()
    filechanger()
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

if __name__ == '__main__':
    auto()