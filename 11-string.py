# characters in string maintain order
# cannot be modified after creation(immutable)
# can loop through characters.
# can be accessed by its position or index 


# new_line ='Line1\nLine2' # \n= newline
# print(new_line)
# tab = 'line1\tLine2'
# print(tab)
# backslash = "C:\\Users\\Name"
# print(backslash)
# quote = "Hello,I am \"Ramesh\""
# print(quote)
# single_quote='hi I am you guide and it\'s day to explain the history'
# print(single_quote)

# bytestring=b'hello'
# print(bytestring)


#  name= input('Enter full name: ')

# result =len(name)

# result = name.find(' ')  return first occurrence of characters.
# result = name.find('c')
# result =name.find('a')

# last occurrence of character
# result = name.rfind('a')

# if character not present then it return -1
# result= name.find('q')

# python will return index of first matching character.
# result =name.rfind('am')

# capitalize()
# result = name.capitalize()

# UPPERCASE
# result = name.upper()

# lowercase
# result = name.lower()

#swapcase() convert each character from lower to upper and vise-versa
# result ='RAM'.swapcase()

# isdigit() only return true if it has all character digit if it has any alpha character it return false.
# isalpha return true if it has only alpha ,no symbol , no digit
# result=name.isalpha()

#count() return number of times a character present in string.
# result = name.count('a')

# replace() 
# result = name.replace(' ','/')


# indexing = accessing elements of a sequence using  [ ](indexing operator) 
# [start : end : step]

credit_number = "1234-5678-9101-1121"
# result =credit_number[0]

text='Ram'
result =text[1]
print(result)

print('www.example.com'.strip('w.m'))

#padding
# the length is getting increased . if the length is same is string it will no affect. 
print("Hello".ljust(10,"x"))
print("Hello".rjust(10))
print('Hello'.center(10)) 
print("Hello".center(7,'@'))
print("Hello".center(20, '*')) 

# padding for number
print('42'.zfill(5))
print('-42'.zfill(5)) # include '-' as a length of character and reduce zero
print('1234'.center(8,'x'))
  
price1 = 3.14159
price2 = -987.567

print(f"price 1 is ${price1:.2f}")
print(f"price 2 is ${price2:.1f}")