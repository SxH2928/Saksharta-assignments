print("The coke cost's 50 cents , and the only coins accepted are:- 25,10,5")
amountDue = 50 
#looping until amountDue is greater than 50...
while amountDue > 0 :
    print("Amount due:",amountDue)
    coin = int(input("Insert coin: "))
    
    if coin in [25,10,5]:
        amountDue -= coin
    
changeOwed = abs(amountDue)

print("change owed:",changeOwed)