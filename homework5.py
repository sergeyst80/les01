import os

cls_str = 'cls' if os.name == 'nt' else 'clear'
users = {'Alex': '111', 'Nike': '222', 'Mike': '333', 'User': 'User', 'Admin': 'Admin'}
current_user = ''
user_password = ''


def authorization(func):
    def wrapper(*args, **kwargs):
        check = users.get(input('Enter user name: '))
        if check is None:
            print('User name is unknown! Access denied!')
        elif check == input('Enter password: '):
            func(*args, **kwargs)
        else:
            print('Password is incorrect! Access denied!')

    return wrapper


@authorization
def func1():
    print('\"Function 1\"')


def func2():
    print('\"Function 2\"')


@authorization
def func3():
    print('\"Function 3\"')


while True:
    os.system(cls_str)
    item = input('Functions menu\n====================\n'
                 + '1 - Function 1 (authorization)\n'
                 + '2 - Function 2\n'
                 + '3 - Function 3 (authorization)\n'
                 + '0 - Exit\n'
                 + 'Your choice: ')
    if item == '0':
        break
    elif item == '1':
        func1()
    elif item == '2':
        func2()
    elif item == '3':
        func3()
    input('Press any key...')
