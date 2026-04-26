# Type casting: converting variable from one data type to another
# str(), int(), float(), bool()

name='Ram'
age=30
numeric_string='1000'
gpa=9.4
is_student=True
num1=0

print(type(name))
print(type(age))
print(type(is_student))
print(type(gpa))

# float to integer
gpa_int= int(gpa)
print(f'The float to int is {gpa_int}')

#integer to float
int_float = float(age)
print(f'integer to float converting {int_float}',type(int_float))

str_float=float(numeric_string)
print(f'numeric string to float {str_float}',type(str_float))

#int to string
int_str = str(age)
print(f'integer to string type casting {int_str}',type(int_str))

#string to int
str_int = int(numeric_string)
print(f'string to integer {str_int}',type(str_int))

# boolean to integer

bol_int = bool(age)
print(f'boolean to integer {bol_int}')
bol_num1=bool(num1)
print(f'integer to boolean {bol_num1}')
bol_str = bool(name)
print(f'string to boolean {bol_str}')