#python calculator

operator = input('Enter an operator (+ - x / % ^ ): ')
num1=float(input('Enter your first Number: '))
num2=float(input('Enter your second Number: '))

if operator == '+':
  print(f'The sum of two number is {round(num1,2) + round(num2,2)}')
elif operator == '-':
  print(f'The difference of two number is {round(num1,2) - round(num2,2)}')
elif operator == 'x':
  print(f'The product of two number is {round(num1,2)* round(num2,2)} ')
elif operator == '/':
  print(f'The divisible of two number  is {round(num1,2)/round(num2,2)} ')
elif operator == '&':
  print(f'The modulo of two number  is {round(num1,2)%round(num2,2)} ')
elif operator == '^':
  print(f'The modulo of two number  is {round(pow(num1,num2),2)} ')