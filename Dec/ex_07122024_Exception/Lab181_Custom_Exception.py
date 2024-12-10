# class CustomException(Exception):
#
#     def __init__(self, message):
#         self.message = message
#         super().__init__(message)
#
# balance = 100
# withdraw = int(input("enter ur withdraw amount\n"))
# if withdraw > 100:
#     raise CustomException ("Low balance")
# else:
#     print("remaining balance", balance - withdraw)

# try:
#     balance = 100
#     withdraw = int(input("enter ur withdraw amount\n"))
#
# if withdraw > 100:
#     except Exception as e:
#         print(e)
# finally:
#     print("remaining balance", balance - withdraw)