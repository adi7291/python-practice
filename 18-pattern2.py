# * 
# * * 
# * * * 
# * * * * 
# * * * * * 

n= int(input('Enter the number: '))

for row in range(1,n+1):
  print('* '*row)

for row in range(1,n+1):
  for column in range(1,n+1):
    if row>=column:
      print('*',end=' ')
    else:
      break
  print('')

for row in range(1,n+1):
  for column in range(1,row+1):
    print('*',end =' ')
  print('')
