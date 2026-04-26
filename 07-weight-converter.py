# weight converter

weight = (input('Enter the weight in (K L): '))
unit = float(input('Enter the unit need to convert into kg or pound: '))
if weight == 'K':
  print(f'{unit} kg is equal to {round(unit*2.205,2)} LBS')
elif weight == 'L':
  print(f'{unit} pound is equal to {round(unit/2.205,2)} KG')
else:
  print('the unit is not defined')