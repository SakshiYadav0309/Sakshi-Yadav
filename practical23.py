# class bank_account:
#    def __init__(self,balance):
#        self.balance = balance
#    def add (self,amount):
#        self.balance += amount
#    def withdraw(self,amount):
#          self .balance -= amount
#    def final_amount(self):
#       return self.balance

# account1 = bank_account(1000)
# account1.add(500)
# account1.withdraw(200)
# print(account1.final_amount()) 

# class bankaccount:
#     def __init__(self,blance):
#         self.blance = blance
#     def add(self,amount):
#         self.blance += amount
#     def withdraw(self,amount):
#         self.blance -= amount
#     def final_amount(self):
#         return self.blance
# initial=int(input("enter your amount:"))
# deposit=int(input("enter your amount:"))
# withdraw=int(input("enter your amount:"))
# account1=bankaccount(initial)
# account1.add(deposit)
# account1.withdraw(withdraw)
# print(account1.final_amount())


#poliymorphism

class police:
    def work(self):
        print("control law & order")
class teacher:
    def work(self):
        print("teaching of students")

class doctor:
    def work(self):
        print("treatment of patients")

xyz=[police(),teacher(),doctor()]

for i in xyz:
    i.work()





































































































