# validate user input exercise
# 1. username is more then 12 characters but at least 8 characters.
# 3. username must not contain spaces
# 4. username must not contain digits
 
user_name = input('Enter a username: ')

if len(user_name)>12:
  print(f'{user_name} is more then 12 character. it must be less then 12 characters and greater then 8 characters')
elif len(user_name)<8:
  print('username must be at least 8 characters')
elif user_name.find(' ') != -1:
  print('user name must not have spaces')
elif user_name.isalpha() == False:
  print('username must have only characters')
else:
  print(f'your username is validated and you can proceed with that username {user_name}.')