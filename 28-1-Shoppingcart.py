# ------YOUR  CART-------
 # Hotdog,apple,hamburger
 # Your Total is: $100.10

foodList = []
priceList =[]
total=0

while True:
  foods =input('Enter the Food You want to purchase (q to quit): ')
  if foods.lower() == 'q':
    break
  else:
    foodList.append(foods)
    price= float(input('Enter the Price of the Food you selected: '))
    priceList.append(price)
print('-----YOUR CART-----') 
for item in foodList:
  print(item.capitalize(),end=' ')
print()
for price in priceList:
  total+=price
print(f'Your Total cart value is ${str(total)}')

