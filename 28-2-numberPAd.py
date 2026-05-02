# we will use tuple for creating number pas in mobile
# we can use list but the list is mutable by using index we can change the value of list
# in Tuple is not mutable.

tup=(
     (1,2,3),
     (4,5,6),
     (7,8,9),
     ('*',0,'#')
     )
for row in tup:
  print(row)
for row in tup:
  for col in row:
    print(col,end='  ')
  print()
