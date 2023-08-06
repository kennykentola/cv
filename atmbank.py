class Bank:
    def __init__(self):
        self.firstname = ""
        self.secondname = ""
        self.accnumber = 0
        self.type = ""
        self.amount = 0
        self.tot = 0

    def setvalue(self):
        print("Enter name: ")
        #self.name = input()
        self.firstname = input('enter the firstname: ')
        self.secondname=input('enter the secondname: ')

        print("Enter Account number")
        self.accnumber = int(input())

        print("Enter Account type")
        self.type = input()

        print("Enter Balance")
        self.tot = int(input())

    def showdata(self):
        print("Name:", self.firstname, self.secondname)
        print("Account No:", self.accnumber)
        print("Account type:", self.type)
        print("Balance:", self.tot)

    def deposit(self):
        print("\nEnter amount to be Deposited")
        self.amount = int(input())

    def showbal(self):
        self.tot += self.amount
        print("\nTotal balance is:", self.tot)

    def withdrawl(self):
        print("Enter amount to withdraw")
        a = int(input())
        avai_balance = self.tot - a
        print("Available Balance is", avai_balance)

# Driver Code
if __name__ == "__main__":
    b = Bank()

    while True:
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("~~~~~~~~~~WELCOME~~~~~~~~~~~~")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("~~~~~~~~~~~~~")
        print("Enter Your Choice")
        print("\t1. Enter name, Account number, Account type")
        print("\t2. Balance Enquiry")
        print("\t3. Deposit Money")
        print("\t4. Show Total balance")
        print("\t5. Withdraw Money")
        print("\t6. Cancel")
        print()
        choice = int(input("enter your choice: "))

        if choice == 1:
            b.setvalue()
        elif choice == 2:
            b.showdata()
        elif choice == 3:
            b.deposit()
        elif choice == 4:
            b.showbal()
        elif choice == 5:
            b.withdrawl()
        elif choice == 6:
            break
        else:
            print("\nInvalid choice")
