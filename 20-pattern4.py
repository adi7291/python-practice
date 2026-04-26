# * * * * * 
#   * * * * 
#     * * * 
#       * * 
#         * 

n = int(input('Enter the number: '))

for row in range(n,0,-1):
  print('  '*(n-row) +'* '*row)


for row in range(n+1,1,-1):
  for column in range(n+1,1,-1):
    if row>=column:
      print('*',end=' ')
    else:
      print(' ',end=' ')
  print('')