#input() ==> A function that prompts the user to enter data. Returns the input data as #string.

name =input('What is your name: ')
print(f'Hello {name}!')
age =input('How old are you? ')

age =int(age)+1
print(f'I am {age} years old.')

#Exercise 2
# Finding the area of rectangle

length= float(input('Enter the length of rectangle: '))
width= float(input('Enter the length of width: '))
area = length * width
print(f'The area of rectangle is {area}cm2')

# Exercise 2 Shopping cart program
item = input('What item you would like to buy?: ')
price=float(input('What is the price of selected item?: '))
quantity = int(input('How many would like to buy?: '))
total = price *quantity
print(f'You have bought {quantity} X {item}/s')
print(f'your total is ${total}')