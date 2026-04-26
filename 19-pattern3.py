# * * * * * 
# * * * * 
# * * * 
# * * 
# * 


n = int(input('Enter the number: '))

for row in range(n,0,-1):
  print('* '*row)

for row in range(n,0,-1):
  for column in range(1,n+1):
    if row>=column:
      print('*',end=' ')
    else:
      break
  print(' ')


