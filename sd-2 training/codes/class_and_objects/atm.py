class BankAccount():
    def __init__ (self) :
        self.account_number=input("enter acc no:")
        self.balance=int(input("enter balance:"))
        self.date_of_opening=input("enter date of opening:")
        self.customer_name=input("enter cust name:")
    def deposit(self,amount):
        self.balance+=amount
        print("\n",amount,"is deposited succesfully\n")
    def withdraw(self,amount):
        if amount>self.balance:
            print("\ninsufficient balance\n")
        else:
            self.balance-=amount
            print("\n",amount,"is withdrawed succesfully\n")
    def check_balance(self):
        print("\nthe account balance is",self.balance,"\n")
user1=BankAccount()
while(True):
    print("1.deposit\n2.withdraw\n3.check balance\n4.Exit")
    num=int(input("enter option:"))
    if num==1:
        user1.deposit(int(input("enter amount:")))
    if num==2:
        user1.withdraw(int(input("enter amount:")))
    if num==3:
        user1.check_balance()
    if num==4:
        break

    
    
    
