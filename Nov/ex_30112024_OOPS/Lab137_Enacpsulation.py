class LoginPage:

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def login(self):
         if self.email == "abhi123@gmail.com" and self.password == "123asbcd":
             print("login is allowed")
         else:
             print("login not allowed")

email = input("enter ur email\n")
password = input("enter ur password\n")

obj_ref = LoginPage(email, password)
obj_ref.login()

# pramod = LoginPage("pramod@gmail.com", "Pass123")
# pramod.login()