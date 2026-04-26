# While loop executes some code until the condition remains true
while True:
  age = int(input('Enter the age: '))

  if age<18:
    print('Not Eligible to vote!!')
  else:
    print('You can vote::')
    break


while True:
  number=int(input('Enter Number between 5-10: '))

  if number<5 or number>10:
    print('Number is not in range.')
  else:
    print(number)
    break