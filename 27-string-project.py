# # take the 16 digit card number and show the message you account XXXX XXXX XXXX 4009 is debited with Rs 1000.Please check your balance.

card=input('Enter 16 digit number: ')
if(len(card)<16):
  print('Please enter 16 digit number') 
  card = int(input('Enter 16 digit number: '))
  
# card = "4455 1122 3344 5566"
clean = card.replace(" ","")
lastFourDigit=card[-4:]
fourDigits = 'X'*4+' '
first12Digits =fourDigits*3
print(first12Digits+lastFourDigit)


