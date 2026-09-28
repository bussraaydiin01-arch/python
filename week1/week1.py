# Create a program which calculate the area of a circle
# from math import pi
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
# r = float(input("Input the radius of the circle : "))
# print("The area of the circle with radius " + str(r) + " is: " + str(pi
# * r ** 2))

from math import pi

r = float(input("Input the radius of the circle: "))
print("The area of the circle is:", pi * r ** 2)

# Create a program that stores an integer, a floating-point number, a string, and a boolean
# variable, and then outputs them.
# Declare and initialize an integer variable `zahl` with the value 10. Check the variable's type
# afterward.
# Declare and initialize a floating-point variable `kommazahl` with the value 10.5. Check the
# variable's type afterward.
# Declare and initialize a string variable `text` with the value "Hello, World!". Check the
# variable's type afterward.
# Declare and initialize a boolean variable `wahrheitswert` with the value True. Check the
# variable's type afterward.
# Output all variables to the console with appropriate descriptions. Check the variable's type
# afterward

zahl = 10
print("zahl:", zahl)
print("Type of zahl:", type(zahl))

kommazahl = 10.5
print("kommazahl:", kommazahl)
print("Type of kommazahl:", type(kommazahl))

text = "Hello, World!"
print("text:", text)
print("Type of text:", type(text))

wahrheitswert = True
print("wahrheitswert:", wahrheitswert)
print("Type of wahrheitswert:", type(wahrheitswert))


# Create a program which will calculate the factorial
# Create a program that converts different data types and outputs the results.
# 1. Convert an integer to a floating-point number.
# number = int(input("Enter a number: "))

number = 10
float_number = float(number)
print(float_number)

# 2. Convert a floating-point number to an integer.
float_number = 10.5
number = int(float_number)
print(number)

# 3. Convert an integer to a string.
number = 10
text = str(number)
print(text)

# 4. Convert a string containing a number to an integer.
text = "20"
number = int(text)
print(number)

# 5. Convert an integer to a Boolean
number = 10
boolean_value = bool(number)
print(boolean_value)