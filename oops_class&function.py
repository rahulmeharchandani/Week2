class student:
    def __init__(self, name, roll_no, marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks
        
    def getdetails(self):
        print(f"Name: {self.name}, Roll_No: {self.roll_no}, Marks: {self.marks}")
        
    def passed(self):
        if self.marks>33:
            print("Pass")
        else:
            print("fail")
            

class bank:
    def __init__(self,name, account_no,balance=0):
        self.name=name            
        self.account_no=account_no
        self.balance=balance
    def deposit(self, amount):
        if amount > 0:
            self.balance+=amount
            print(f"Deposited: {amount}. New balance: {self.balance} ")
        else:
            print("Invalid amount")
    def withdraw(self,amount):
        if 0<amount<=self.balance:
            self.balance-=amount
            print(f"Withdrawn: {amount}. Remaining balance: {self.balance}")
        else:
            print("Insufficent balance")
    def showb(self):
        print(f"Current Balance: {self.balance}")                    
                      
                    
            
student1=student("rahul",21,70)
student1.getdetails()
print(student1.passed())  

account1=bank("Rahul","1245",7000)
account1.showb()
account1.deposit(700)
account1.withdraw(500)
account1.showb()                     