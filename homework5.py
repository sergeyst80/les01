import os

clr_str = 'cls' if os.name == 'nt' else 'clear'
users = {'alex': '111',
         'nike': '222',
         'mike': '333',
         'user': 'user',
         'admin': 'admin'}


def clr_scr():
    os.system(clr_str)


def authorization(func):

    def wrapper(*args, **kwargs):
        check = users.get(input('Enter user name: ').lower())

        if check is None:
            print('User name is unknown! Access denied!')
        elif check == input('Enter password: '):
            clr_scr()
            value = func(*args, **kwargs)
        else:
            print('Password is incorrect! Access denied!')
        
        return value

    return wrapper


@authorization
def func1():
    print('\"Function 1\"')


def func2():
    print('\"Function 2\"')


@authorization
def func3():
    print('\"Function 3\"')


functions = {'1': func1,
             '2': func2,
             '3': func3}

while True:
    clr_scr()
    item = input('Functions menu\n====================\n'
                 + '1\t- Function 1 (authorization)\n'
                 + '2\t- Function 2\n'
                 + '3\t- Function 3 (authorization)\n'
                 + 'Other\t- Exit\n'
                 + '====================\n'
                 + 'Your choice: ')
    clr_scr()

    if functions.get(item) is not None:
        functions[item]()
    else:
        break

    input('Press \'Enter\'...')
