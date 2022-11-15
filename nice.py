quantity=int(input("how much would you like to buy for 100 per quanity"))

if quantity * 100 > 1000:
  print("Cost is",((quantity*100)-(.1*quantity*100)))
else:
  print("Cost is",quantity*100)
