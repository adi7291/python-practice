# variables are container for value (string,integer, float,boolean)

#string
first_name = "Ram"
food ='Dal bhat chokha'
email="ram@gamil.com"
print(first_name)
print(f"Hello {first_name}")
print(f'you like {food}')
print(f'your email is {email}')

#Integers
age=30
print(f'{first_name} your age is {age}.')

#Float
price =99.99
print(f"This price of the selected item is ${price}")

#Boolean
for_sale=True
is_online=False
if age>18:
  print(f'You are eligible for vote')
else:
  print('you are not eligible.')

if for_sale:
  print('You will get discount')
else:
  print('Not for sale')

if is_online:
  print('you are online')
else:
  print('you are offline.')
