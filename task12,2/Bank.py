class Bank :
    def __init__(self,username):
        self.username=username
    def options(self):
        print("chosse what do u want \n1) creat an acount \n2) sign in \n3) show your balance \n4) deposit money \n5) withdraw money \n6) transfer money \n7) Exit")
    def creatacount(self,database):
        balance=0
        username=input("Enter your username: ")
        database[username]={"balance":balance}
    def signin(self,database):
        username=input("Enter your username: ")
        if username == database[username]:
            print("Hello",database[username])
        else :
            print("Sorry but u have to creat an acoount first")
    def showbalance(self , database,username):
        print(database[username]["balance"])
    def depositmoney(self ,database,username):
        balance =int(input("Enter how much do u want to deposit: "))
        database[username]={"balance":balance}
    def withdrawmoney(self,database,username):
        balance =int(input("Enter how much money do u wan!: "))
        balance -= database[username]["balance"]
    def transfermoney(self,database):
        username=input("Please enter the user's bank acount to transfer money: ")
        if username == database[username]:
            balance=int(input("Enter how much do u want to transfer: "))
            if balance > database[username]["balance"]:
                print("u don't have that much money ^_____^!!")
            else :
                database[username]["balance"] -= balance
        else :
            print("The username is not found 🕵️‍♂️!!")
#sorry that i have yo leave u in this on u but please 🙏 do your best and i'm with u if u need any thing just text me
