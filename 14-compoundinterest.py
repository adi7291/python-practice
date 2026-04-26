
while True:
  principle = float(input('Enter you principle: '))
  if principle<0:
    print('Principle con not be negative')
  else:
    break

while True:
  rate=float(input('Enter rate in %: '))
  if rate<0:
    print('Rate can not be negative.')
  else:
    break

while True:
  time=float(input('Enter time: '))
  if time<0:
    print('time can not be negative.')
  else:
    break
total = principle*pow((1+rate/100),time)
print(f'The total amount after {time} year/s is {total:.2f}')