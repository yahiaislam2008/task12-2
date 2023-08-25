from Bank import Bank
database={}
bank=Bank("account")
while True :
    bank.options()
    choice=int(input("Enter your choice: "))
    if choice < 8 or choice >0:
        if choice ==1:
            bank.creatacount(database)
            #todo class for Customer
            #pass#deleted
        elif choice ==2:
            bank.signin(database)
            #todo class for Customer
            #pass#deleted
        elif choice ==3:
            bank.showbalance(database)
        elif choice ==4:
            bank.depositmoney(database)
        elif choice ==5:
            bank.withdrawmoney(database)
        elif choice ==6:
            bank.transfermoney(database)
        elif choice ==7:
            break
    else :
        break
#sorry that i have yo leave u in this on u but please 🙏 do your best and i'm with u if u need any thing just text me