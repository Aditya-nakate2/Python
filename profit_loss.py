cp=float(input("Enter the cost prise:"))
sp=float(input("Enetr the selling prise:"))

#if sp is more than cp then we get profit.
if sp> cp:
    profit=sp-cp
    print("we get the profit of:",profit)

#if cp is more than sp then we get loss.   
elif cp>sp:
    loss=cp-sp
    print("we get the loss of:",loss)

#if sp and cp is equal, then we don't have any profit or loss.
else:
    print("We dont have loss or profit")


