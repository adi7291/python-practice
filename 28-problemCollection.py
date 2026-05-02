#Remove duplicates but keep order
nums = [1,2,2,3,4,3,5]
# expected: [1,2,3,4,5]

nonDuplicateList = []

for item in nums:
  if item not in nonDuplicateList:
   nonDuplicateList.append(item)
print(nonDuplicateList)

# Find second largest number
numList = [10, 20, 5, 8, 20]
removeDuplicateFromList = list(set(numList))
print(removeDuplicateFromList)
removeDuplicateFromList.sort()
print(removeDuplicateFromList[-2])
