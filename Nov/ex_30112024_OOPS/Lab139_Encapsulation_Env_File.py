
# Web Automation - ex_11012025_SeleniumTest
# Page - You are going automate

from dotenv import load_dotenv
import os
class VWOLoginPage:

    def __init__(self, email_arg, password_arg):
        self.email = email_arg
        self.password = password_arg

    def login_confirm(self):
        if self.email == "abhi123@gmail.com" and self.password == "Pass123":
            print("Allowed, Login Success")
        else:
            print("Login Failed")

load_dotenv()
email = os.getenv("email")
password = os.getenv("pass")

print(email, password)
vwo_obj = VWOLoginPage(email, password)
vwo_obj.login_confirm()
