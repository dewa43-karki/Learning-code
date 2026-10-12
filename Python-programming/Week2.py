# Simple program to print my name, age and city.
name = "Karki Dewa"
age = "19"
city = "Lalitpur, Nepal"

print("Hie, I'm ", name + ", and my age is", age + ".", "I'm from ", city )

age = 10

print("Hie, I'm", name + ", and my age is", age, "I'm from", city)



# Simple program to calculate balance after deposit and withdrawal.
balance = 1000
print("Opening balance :", balance)

balance = balance + 500
print("After deposit :", balance)

balance = balance - 200
print("After withdrawal :", balance)

balance *= 2
print("After doubling :", balance)



# Simple program to calculate area and perimeter of a room.
print("--- Area Calculator ---")

length = float(input("What is the lenght of the room?"))
width = float(input("What is the width of the room?"))

area = length * width

print("The area of the room:", area)

perimeter = (2 * (length + width))

print("The perimeter of the room:", perimeter)



# Simple program to calculate the total score after doubling the score and adding 100.
name = "Ha-eun" 
Age = 20
print("Age is:", Age) 
score = int(input("Enter your score: "))
print("Doubled:", score * 2) 
print("Total: ", score + 100)



# Simple program to calculate the total price of an item after tax.
print("=" * 40)

print("       Dewa dd's Shop")

print("=" * 40)

item = input("Item name: ")
price = int(input("Unit price: "))
quantity = int(input("Quantity: "))

subtotal = price * quantity
tax = subtotal * 0.1
total= subtotal + tax

print("Item         :", item)
print("Quantity     :", quantity)
print("Sub-total    :", subtotal)
print("Tax(10%)     :", tax)
print("Total        :", total)

print("-" * 40)



# Simple program to print student profile.
name = input("Name: ")
age = int(input("Age: "))
city = input("Address: ")

print("-" * 40 )
print("         Student Profile")

print("Name: ", name)
print("Age: ", age)
print("Address: ", city)

print("-" * 40 )



# Simple program to calculate the average of two numbers.
nub1 = int(input("Enter any number: "))
nub2 = int(input("Enter another number: "))

average = ( nub1 + nub2 )/ 2

print("The average of those number are ", average)



# Simple program to convert Celsius to Fahrenheit.
c= int(input(" Enter the temperature in Celsius: "))

f = (9/5 * c) + 32

print("The temperature in Fahrenheit: ", f)



# Simple program done see the error in the code.
num = input("Enter any number: ")

add = num + 5

print(add)

# { the output is:
# Enter any number: 6
# Traceback (most recent call last):
#   File "c:\Users\acer\OneDrive\Documents\Downloads\python\Dewa dd\hw4.py", line 3, in <module>
#     add = num + 5
#           ~~~~^~~
# TypeError: can only concatenate str (not "int") to str 


