def tip(amount,percent):
   amount=amount+amount*(percent/100)
   return round(amount,2)

bill=float(input("How much was the meal?\n"))
Tip=float(input("What percent would you like to tip\n"))

Total = tip(bill,Tip)

print("Leave = ",Total )