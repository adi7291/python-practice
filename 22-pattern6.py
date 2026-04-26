#  * * * * *
#   * * * *
#    * * *
#     * *
#      *
n = int(input('Enter the number: '))

for row in range(n,0,-1):
  print(' '*(n-row)+' *'*row)

for row in range(1,n+1):
  for col in range(1,n+1):
    if row<=col:
     print('*',end=' ')
    else:
     print('',end=' ')
  print('')

