print('Temperature converter!!')

temperature_value = float(input('Enter a value temperature: '))
choice = input('Enter the temperature in (C K F): ')

if choice == 'C':
  celsius_to_kelvin = temperature_value+273.15
  print(f'The temperature in kelvin is {celsius_to_kelvin} K')
  celsius_to_fahrenheit = (temperature_value*9/5) +32
  print(f'Temperature in Fahrenheit is {celsius_to_fahrenheit} ')
elif choice == 'K':
  kelvin_to_celsius = temperature_value-273.15
  print(f'Temperature in degree celsius is {kelvin_to_celsius} C')
elif choice == 'F':
 fahrenheit_to_celsius = (temperature_value-32)*5/9
 print(f'The temperature in degree celsius is {fahrenheit_to_celsius} C ')
else:
  print(f'Invalid temperature choice')
