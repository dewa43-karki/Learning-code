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
