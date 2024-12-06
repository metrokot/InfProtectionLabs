import hashlib
import random

class User():
    def __init__(self, params):
        print(params)
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
    if lastpass != user.password:
        error = 'Неверный предыдуший пароль'
    if newpass != confirmpass:
        error = 'Неверное подтверждение пароля'
    if not setpasswordcheck(newpass):
        error = 'Не соблюдены ограничения на пароль'
    if not error:
        with open('users.txt', 'r') as f:
            old_data = f.read()
        new_data = old_data.replace(f'{user.login}|{user.password}', f'{user.login}|{newpass}')
        with open('users.txt', 'w') as f:
            f.write(new_data)
    return error


def newUser(login):
    f = open("users.txt", 'a')
    f.write(f'{login}||user|0|0' + '\n')
    return True


def UserList():
    f = open("users.txt", 'r')
    f1 = open('users2.txt','w')
    userList = []
    for line in f:
        user = User(line.strip().split('|'))
        userList.append(user)
    f.close()
    f1.close()
    return userList


def filechanger():
    f = open("users.txt", 'w')
    f1 = open('users2.txt', 'r')
    content = f1.read()
    f.write(content)
    f.close()
    f1.close()


def predobrabot():
    f = open('users.txt', 'r')
    f2 = open("users2.txt", 'w')
    for line in f:
        if line!='\n' and line!='' and line!=None:
            f2.write(line)
    f.close()
    f2.close()
    filechanger()

def setpasswordcheck(password):
    tr=0
    numb = list('1234567890')
    zn = list(',.?!;')
    zn2 = list('/*-+>=%^')
    for elem in numb:
        if elem in password:
            tr+=1
            break
    for elem in zn:
        if elem in password:
            tr+=1
            break
    for elem in zn2:
        if elem in password:
            tr+=1
            break
    if tr==3:
        return True
    else:
        return False


def psevdoshifrSHA():
    f = open('users.txt', 'r')
    data = f.load()

def shifrSHA():
    hash = lambda data, salt: hashlib.sha256((salt + data).encode()).hexdigest()
    f = open('users.txt', 'r')
    blocks = [line for line in f]
    f.close()
    salt = str(random.randint(1, 1000000))
    hashed_blocks = [hash(block, salt) for block in blocks]
    combined_hash = hashed_blocks[0]
    for block_hash in hashed_blocks[1:]:
        combined_hash = hash(combined_hash, block_hash)
    f = open('input.txt', 'w')
    f.write(combined_hash)
    '''
    file_path = 'example.txt'
    
    with open(file_path, 'rb') as file:
        while True:
            data = file.read(1024)
            if not data:
                break
            md5_hash.update(data)
            sha256_hash.update(data)
    
    print(f'MD5: {md5_hash.hexdigest()}')
    print(f'SHA-256: {sha256_hash.hexdigest()}')
    '''
def unshifrSHA():
    pass
def psevdoshifrMD5():
    hash = lambda data, salt: hashlib.md5((salt + data).encode()).hexdigest()
    f = open('users.txt', 'r')
    blocks = [line for line in f]
    f.close()
    salt = str(random.randint(1, 1000000))
    hashed_blocks = [hash(block, salt) for block in blocks]
    combined_hash = hashed_blocks[0]
    for block_hash in hashed_blocks[1:]:
        combined_hash = hash(combined_hash, block_hash)
    f = open('input.txt', 'w')
    f.write(combined_hash)
def unshifrMD5():
    pass

def keypass(key):
    if key == 'pass':
        return True
    else:
        False
