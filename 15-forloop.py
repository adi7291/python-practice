
# for x in range(0,5):
#   print(x)
#   if x==3:
#     break
#   print(x*2)
# print('Loop terminated')

# for x in range(0,5):
#   print(x)
#   if x==3:
#     continue
#   print(x*2)
# print('Loop terminated')

# for x in range(0,5):
#   print(x)
#   if x==3:
#     break
#   print(x*2)
# else:
#   print('a')





# for loop::: executes block of code fixed number of times.

# for x in range(1,12,2):
#   print(x)

# credit_card ="1234-2345-3456-4567"

# for x in credit_card:
#   print(x)

# for x in range(1,21):
#   if x==13:
#     continue
#   else:
#     print(x)
# for x in range(1,11):
#   if x==6:
#     break
#   else:
#     print(x)
# n=100
# for i in range(2,n):
#   for j in range(2,i):
#     if(i%j==0):
#       break
#   else:
#     print(i)

for n in range(1,101):
  count=0
  for i in range(1,n+1):
    if(n%i==0):
      count+=1
    if count>2:
        break
  if count==2:
    print(n)
