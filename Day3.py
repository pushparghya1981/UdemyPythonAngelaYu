# Variables, DataTypes & Typecasting

# Variables
# string
var1 = 'abc'
# integer
var2 = 4
# float
var3 = 36.7
var4 = 'def'

# DataTypes
# <class 'str'>
print(type(var1))
# <class 'int'>
print(type(var2))
# <class 'float'>
print(type(var3))

# we concatenate strings
print(var2+var3)
# we add numbers
print(var1+var4)

# Type casting
var5 = "56"
var6 = "99"
print(int(var5)+int(var6))

# Print Hello World 5 times in a single line
print("Hello World "*5)

# Print Hello World 5 times in each new line
print("Hello World \n"*5)

# print sum of var2+var3 into string & print 5 times
print(5*str((var2+var3)))

# taking user input
print("Enter your number :")
input_num = input()
print("You entered : ", input_num)
print("Entered num +10 =", int(input_num)+10)

# Calculator - adds 2 numbers taking inputs of 2 numbers
print("Enter 1st number :", end="")
num1 = input()
print("Enter 2nd number :", end="")
num2 = input()
print("Sum :", int(num1)+int(num2))

text = "100"
print(float(text))
