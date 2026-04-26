num =5

print( "Positive" if num>0 else "Negative")

# number is even or odd

result = num % 2

print("Even" if result==0 else "odd")

# max of two number::
num1 =int(input('Enter first number: '))
num2 =int(input('Enter second number: '))
print(f'{num1} is max' if num1>num2 else f'{num2} is max')

# min of two number
min_num =num1 if num1<num2 else num2
print(f'minimum of two number is {min_num}')
age=input('Enter your age: ')
status = 'Adult' if age>18 else 'child' 
print(f'your age is {status}')