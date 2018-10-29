users_list = [{'username':'tom', 'role':'lf', 'password':'password'},
         {'username': 'julius', 'role': 'lfa', 'password': 'password1', 'team':'ta'},
         {'username': 'angela', 'role': 'lfa', 'password': 'password1', 'team':'tb'},
         {'username': 'baker', 'role': 'bootcamper', 'password': 'password2', 'team':'ta'},
         {'username': 'arnold', 'role': 'bootcamper', 'password': 'password2', 'team':'ta'},
         {'username': 'ricky', 'role': 'bootcamper', 'password': 'password2', 'team':'tb'},
         {'username': 'daphne', 'role': 'bootcamper', 'password': 'password2', 'team':'tb'}]


class User:
	def __init__(self, name, password):
		self.name = name
		self.password = password

	def login(self):
		user = next(filter(lambda x: x['username'] == self.name and x['password'] == self.password, users_list), None)
		if not user:
			print ('Not success')
		if user:
			return 'success'


def login_func():
	response = ""
	
	while response != 'success':
		_name = input('provide username: ')
		passcode = input('provide password: ')
		user = User(_name, passcode)
		response = user.login()


login_func()
