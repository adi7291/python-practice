import math
#  Find the circumference of circle.

radius=float(input('Enter the radius of circle: '))

circumference = 2*math.pi*radius
area = math.pi*pow(radius,2)
print(f'Circumference of circle is {round(circumference,2)}cm and area is {round(area,2)}cm^2')

#calculate the hypotnous of right angle triangle

a =float(input('Enter the side a: '))
b = float(input('Enter the side b: '))

c=math.sqrt(pow(a,2)+pow(b,2))
print(f'hypotaneous of right angled triangle is {round(c,2)}')