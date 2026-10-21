# Program that shows why we need functions
s1, s2, s3 = 92, 78, 85
print("Ha-eun's average:", (s1 + s2 + s3) / 3)
 
s1, s2, s3 = 55, 88, 64
print("Minjun's average:", (s1 + s2 + s3) / 3)
 
s1, s2, s3 = 70, 95, 82
print("Ji-woo's average:", (s1 + s2 + s3) / 3)



# The Simplest Possible Function
def greet():                  
    print("Hello!")           
    print("Welcome to Python.")
 
print("Program started")     
 
greet()                     
greet()                       
print("Program finished")



# Functions That Take Information
def greet(name):            
    print("Hello,", name, "!")
 
greet("Ha-eun")              
greet("Minjun")               
greet("Ji-woo")
 
def introduce(name, age):   
    print(name, "is", age, "years old")
 
introduce("Ha-eun", 20)        



# Real-World Example: A Café Receipt
def print_line():
    print("-" * 32)
 
def receipt_row(item, qty, price):          
    print(item, "x", qty, "=", qty * price, "won")
 
print_line()
receipt_row("Americano", 2, 4500)          
receipt_row("Croissant", 1, 3800)
receipt_row("Latte", 3, 5000)
print_line()



# Program with the return statements
def average(a, b, c):
    total = a + b + c 
    return total / 3 


print("Ha-eun's average :", average(92, 78, 85))

print("Minjun's average :", average(55, 88, 64))

print("Ji-woo's average :", average(70, 95, 82))

top = average(92, 78, 85)

if top >= 80:
    print("That is a strong average!")



# Program that returns more than one value
def get_two_numbers():
    a = float(input("First number : "))
    b = float(input("Second number: "))
    return a, b 

x, y = get_two_numbers()
print("You entered", x, "and", y)

def stats(a, b, c):
    total = a + b + c
    return total, total / 3 

t, avg = stats(10, 20, 30)

print("Total:", t, "| Average:", avg)



# Building a program from several functions
def get_score():
    return float(input("Enter a score (0-100): "))

def score_to_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def show_result(score, grade):
    print("Score:", score, "→ Grade:", grade)

score = get_score()
grade = score_to_grade(score)
show_result(score, grade)



# Real-World Example: Splitting the Bill
def split_bill(total, people, tip=0.10):
    with_tip = total + total * tip
    return with_tip / people 

share = split_bill(60000, 4)
print("Each person pays:", share, "won")
print("With a 15% tip:", split_bill(60000, 4, 0.15), "won")

if share > 15000:
    print("A bit expensive tonight!")



# Program to understand the error
def calculate():
    result = 100 * 2 # 'result' is LOCAL to this function
    print("Inside function:", result)

calculate()

def calculate_v2():
    result = 100 * 2
    return result 

answer = calculate_v2() 
print("Outside function:", answer)



# Program that print a right angle triangle of stars
rows = int(input("How many rows? "))
print()

print("The different type of right angled triangle of star")
print() 
for i in range(1, rows + 1):       
    for j in range(i):             
        print("*", end="")         
    print()     
print()
print()

for i in range(1, rows + 1):
    print(" " * (rows - i), end = "")
    for j in range(i):
        print("*", end = "")
    print()



# Program that print pyramif shaped stars
rows = int(input("Enter numbers of rows: "))
print()

print("The pyramid shaped star pattern:")
for i in range(1, rows + 1):
    print(" " * (rows - i), end = "")
    for j in range(( 2*i)-1 ):
        print("*", end = "")
    print()



# Program that print a diamond shaped stars
rows = int(input("Enter how many rows: "))
print()

print("A diamond shaped star pattern: ")
for i in range (1, rows + 1):
    print(" " * (rows - i), end = "")
    for j in range ((2 * i) - 1):
        print("*", end = "")
    print()
for i in range (rows - 1, 0, -1):
    print(" " * (rows - i), end = "")
    for j in range ((2 * i) - 1):
        print("*", end = "")
    print()



# Program that print square and rectangle shaped stars
rows = int(input("Enter how many rows: "))
print()

print("A square shaped star pattern: ")
for i in range(rows):
    for j in range(rows):
        print("*", end = "")
    print()

print()

# for a nrectangle
rows = int(input("Enter the numbers of rows      : "))
column = int(input("Enter the number of columns: "))
print()

print("A rectangle shaped star pattern: ")
for i in range(rows):
    for j in range(column):
        print("*", end = "")
    print()



# Program that returns true or false for a given prime number
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

print(is_prime(7))



# Temperature converter made using at least two functions
def temperature():
    print("  Temperature Converter   ")

def tem_conv(c):
    f =  c * 9/5 + 32 
    return f

temperature()
print()
celsius = float(input("Enter the temperature in Celsius: "))
fahrenheit = tem_conv(celsius)
print(f"{celsius}°C = {fahrenheit}°F")



# Rewriting week 4s' program using functions
def number(n):
    if n == 0:
        return "Zero"
    elif n > 0:
        return "Positive"
    else:
        return "Negative"


print(number(4))



# Program of function that takes three scores and returns the highest.
def num(a,b,c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

nub1 = int(input("Enter 1st score: "))
nub2 = int(input("Enter 2nd score: "))
nub3 = int(input("Enter 3rd score: "))

greatest = num( nub1, nub2, nub3)
print(f"The greatest score among them is {greatest}. ")


