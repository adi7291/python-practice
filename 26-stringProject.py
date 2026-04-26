

for x in range(2):
  foodList = input('Enter the name of food')
  priceList=input('Enter the Price')
  dashes = 10-len(foodList)-len(priceList)
  print(foodList +'-'*dashes+ priceList)