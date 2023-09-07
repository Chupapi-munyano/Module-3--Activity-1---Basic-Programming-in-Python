Sa = int(input("Sandwich 50 each\nIced tea 10 each \nPlease enter the number of sandwich: "))
Ic = int(input("Please enter the number of iced tea: "))
Sa_price = 50 * Sa
Ic_price = 10 * Ic
bill =  Sa_price + Ic_price
Pay_am = int(input("Please enter the payment amount "))
Change = Pay_am - bill
print ("Your change is " + str(Change))
