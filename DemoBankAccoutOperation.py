#create a new ac
#deposit the money
#withdraw the money
#Balance enquery

class Bank:
    bankName="Oriental Bank Of Commerce"

    def __init__(self, acNo, acName, acBalance ):
        self.acNo=acNo
        self.acName=acName
        self.acBalance=acBalance

    def deposit(self,acNo, acBalance):
        if(self.acNo==acNo):
            self.acBalance= self.acBalance+acBalance
            print(" Balance is deposited successfully \n Your total balance is ",self.acBalance)
        else:
            print("Account No is not valid")
    
    def withdraw(self, acNo, acBalance):
        if(self.acNo==acNo):
            if(self.acBalance<acBalance):
                print("You do not have sufficent balance in your Account")

            else:
                self.acBalance-=acBalance
                print("You have withdrawn ",acBalance," from your Account")
                print("Thank for Transiction")
        else:
            print("Invalid Account No ")
    
    def balanceEnquery(self,acNo):
        if(self.acNo==acNo):
            print(" Your Current balance is ",self.acBalance)
        else:
            print("Invalid Account No")
    
print("Welcome to ", Bank.bankName)
acNo=input("Enter the Account No")
acName=input("Enter the Account Name")
acBalance=int(input("Enter initial Balance"))
aviAccount = Bank(acNo,acName,acBalance)

print("Account is created successfully")
print("Thank For account creation with us")

ch=0
while ch !=4:
    print(" Enter 1 for Deposit")
    print(" Enter 2 for Withdraw")
    print(" Enter 3 for Balance Enquery")
    print(" Enter 4 for Exit")

    ch= int(input())
    if(ch==1):
        acNo=input("Enter the Account No:")
        acBalance=int(input("Enter amount to deposit:"))
        aviAccount.deposit(acNo,acBalance)
    elif(ch==2):
        acNo=input("Enter the Account No:")
        acBalance=int(input("Enter amount to withdraw:"))
        aviAccount.withdraw(acNo,acBalance)
    elif(ch==3):
        acNo=input("Enter the Account No:")
        aviAccount.balanceEnquery(acNo)
    elif ch==4:
        pass
    else:
        print("Invalid choice")

