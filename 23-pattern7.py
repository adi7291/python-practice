#          * 
#         * * 
#        * * * 
#       * * * * 
#      * * * * * 
#     * * * * * * 
#    * * * * * * * 
#   * * * * * * * * 
#  * * * * * * * * * 
# * * * * * * * * * * 

n = int(input('Enter the number: '))

for row in range(1,n+1):
  print(' '*(n-row)+'* '*row)
