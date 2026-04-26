import time 

my_time=int(input('Enter time in seconds: '))
for x in range(my_time,0,-1):
  seconds = int(x%60)
  minutes=int(x/60)%60
  hours =int(x/3600) %24
  days = int(x/(24*3600))%30
  time.sleep(1)
  print(f'{hours:02}:{minutes:02}:{seconds:02}')

print('Times Up!!')


given_time = int(input('Enter the time in second: '))
current_time =0
for x in range(given_time+1):
  minutes=int(x/60)%60
  seconds = int(x%60)
  hours = int(x/3600)
  print(f'{hours:02}:{minutes:02}:{seconds:02}')
  time.sleep(1)