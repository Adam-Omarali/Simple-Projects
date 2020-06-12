# class BankAccount(object):
#     balance = 0
#
#     def __init__(self, name):
#         self.name = name
#
#     def __repr__(self):
#         return self.name + ", You have %d money in your account." % self.balance
#
#     def show_balance(self):
#         print(str(self.balance))
#
#     def deposit(self, amount):
#         if amount <= 0:
#             print("Error, You can't deposit less than zero dollars")
#
#         else:
#             print(str(amount))
#             self.balance += amount
#             self.show_balance()
#
#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Error, you don't have that much money in your account")
#
#         else:
#             print(str(amount))
#             self.balance -= amount
#             self.show_balance()
#
#
# my_account = BankAccount("Adam")
# print(my_account)
# print(my_account.show_balance())
# my_account.deposit(2000)
# my_account.withdraw(1000)
# print(my_account)






