#Checking a value's type 
print(type(20))
print(type(19.99))
print(type("Dewa"))
print(type(True))

age = 19
name = "Ktm"
print(type(age), type(name))

print(type(20))
print(type("20"))



# Integers and floats
student = 43
temperature = -5
print(student, temperature)

price = 19.99
whole = 2.0
print(type(whole))

result = 10 + 2.5
print(result, type(result))

result = 10 / 2.5
print(result, type(result))



# Strings: Text Values
name = "Dewa"
city = "Ktm"
print(name, city)

quote = "hie"
title = 'She said "How you doing?" to me'
print(quote)
print(title)

print(len(name))
print(name * 2)
print(name + " from " + city)



# Booleans: True and False
is_enrolled = True
is_finished  = False
print(is_enrolled, type(is_enrolled))

print(10 > 5)
print(10 == 5)

result = None
print(result, type(result))



# Converting between types
age_text = "19"
age = int(age_text)
print(age + 5)

score = 95
message = "Your score is " + str(score)
print(message)

print(int(7.9))
print(round(7.9))

import math
print(math.ceil(5.3))
print(math.floor(5.3))



# Putting it together: A cafe receipt
item = "Caramel Smoothie & Jhol Momo"
price = 2800.0 + 2500.0
quantity = int(input("How many?"))

subtotal = quantity + price

print("Item       :", item)
print("Quantity   :", quantity)
print("Subtotal   :", subtotal, " won")

print("Thank you! " + str(quantity) + " food ordered. ")
print("     Come again")



# Students Average Calculator
print("     Studnets Average Calculator     ")

name = "Helkare"
faculty = "SC Fall 26"

mark1 = float(input("Enter the marks of 1st subject: "))
mark2 = float(input("Enter the marks of 2nd subject: "))
mark3 = float(input("Enter the marks of 3rd subject: "))
mark4 = float(input("Enter the marks of 4th subject: "))
mark5 = float(input("Enter the marks of 5th subject: "))
print()

print("Name              : ", name)
print("Faculty           : ", faculty)

total = mark1 + mark2 + mark3 + mark4+ mark5
average = total/ 5
print("Total marks       : ", total)
print("Average marks     : ", average)


# Precedence in Practice
print(2 + 3 * 4)
print((2 +3) * 4)

print(2 * 3 ** 2)
print((2 * 3) ** 2)

print(100 / 5 *2)

subtotal = 100
tax_rate = 0.1
total = subtotal + (subtotal * tax_rate)
print(round(total, 2))



# Comparison operators in action
age = 19
print( age == 19 )
print( age != 19 )
print( age > 18 )
print( age <= 18 )

is_adult = age >= 18
print( is_adult, type(is_adult))


# Investigate type and conversion
a = 20
b = 20.0
c = "20"

print(type(a))
print(type(b))
print(type(c))

print( a*2 )
print( c*2 ) 

c= int(c*2)
print( a*2 >= c*2 )
print( a*2 <= c*2 ) 

c = int(c) 
print( c *2 )

print( a == b)
print( a == c)


# Build a Grade Checker
print()
print("              RESULT CHECKER      ")
print()

score = float(input("Enter your score                         : "))
attendance = float(input("Enter your attendance percentage %       : "))

passed_exam = score >= 60
good_attendance = attendance >= 75

can_pass = passed_exam and good_attendance

print("Passed Exam      : ", passed_exam)
print("Good Attendance  : ", good_attendance)
print("Can Pass         : ", can_pass)



# Find and fix mistake
price = float(input("Enter the price: "))
total = price * 3 

is_cheap = total < 10000
print("Cheap?", is_cheap)

count = 7
print("Even?", count % 2 == 0) 

found = True

print("Total: ",  total)



# Build a time converter
print("=" * 34)
print("       Time Converter ")
print("=" * 34)

total = int(input("Enter a number of seconds : "))

hours = total // 3600
min = ( total % 3600 ) // 60
sec = total % 60

print ( hours, " hrs", min, " min", sec, " sec")
print (" Even : ", (total % 2) == 0 )
