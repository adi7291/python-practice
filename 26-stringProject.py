foodList = input('Enter the name of food')
priceList=input('Enter the Price')
dashes = 5-len(foodList)-len(priceList)

print( )
print(foodList +'-'*dashes+ priceList)