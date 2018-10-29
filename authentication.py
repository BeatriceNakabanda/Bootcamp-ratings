users = [{'username': 'tom', 'role': 'lf', 'password': 'password'},
              {'username': 'julius', 'role': 'lfa',
                  'password': 'password1', 'team': 'ta'},
              {'username': 'angela', 'role': 'lfa',
                  'password': 'password1', 'team': 'tb'},
              {'username': 'baker', 'role': 'bootcamper',
               'password': 'password2', 'team': 'ta'},
              {'username': 'arnold', 'role': 'bootcamper',
               'password': 'password2', 'team': 'ta'},
              {'username': 'ricky', 'role': 'bootcamper',
               'password': 'password2', 'team': 'tb'},
              {'username': 'daphne', 'role': 'bootcamper', 'password': 'password2', 'team': 'tb'}]

class User:
    def __init__(self, username, role, password):
       self.username = username
       self.password = password
       self.role = role

    def login(self):
        for user in users:
            if user['username'] == self.username and user['password'] == self.password:
                if user['role'] == 'lfa':
                    return self.login_lfa()
                elif user['role'] == 'bootcamper':
                    self.login_bootcamper()
                else:
                    return 'invalid role'
        return "Your login is invalid"

    def login_bootcamper(self):
        print('you are logged in as a bootcamper')
    
;    def login_lfa(self):
        print('you are logged in as an lfa')


if __name__ == '__main__':
    username = input("Please input username : ")
    role = input("Please input role : ")
    password = input("Please input password : ")

    if role == 'lfa':
        lfa = User(username, 'lfa', password)
        print(lfa.login())
    elif role == 'bootcamper':
        bootcamper = User(username, 'bootcamper', password)
        print(bootcamper.login())
    else:
        print('invalid role')

