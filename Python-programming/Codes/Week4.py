# Simplest possible if
if 20 > 10:
    print(" 20 is greater")

print("Program finished")



# When the condition is false
if 20 > 10:
    print("A: this runs")

if 5 > 10:
    print("B: this does NOT run")

print("C: this always runs")



# Making the decision interactive
age = int(input("Enter your age: "))

if age >= 18:
    print("You are an Adult.")

print("Age recoreded: ", age)



# Two seperate ifs vs if-else
age = 34

if age >= 18:
    print("Adult")

if age < 18:
    print("Minor")

age = 43

if age >= 18:
    print("Adult")

if age < 18:
    print("Minor")



# The simplest if-else
number = 7

if number > 5:
    print("Greater than 5")
else:
    print("5 or less")

print("Done")



# The simplest if-elif-else
number = 0

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")




# Building a temperature's checker
temperature = int(input("Enter the temperature: "))

if temperature > 30:
    print("Its hot today")

if temperature < 0:
    print("Freezing!")
    print("Wear a coat")

print("Temperature recorded ", temperature)



# Odd or Even, Pass or Fail
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Its a even number.")
else:
    print("Its a odd number.")


score = float(input("Enter an exam score: "))

if score >= 60:
    print("Passed")
else:
    print("Failled")



# Build a Grade Calculator
print("--- GRADE CALCULATOR ---")
print()

score = float(input("Enter an exam score: "))

if score >= 90:
    grade = "A"
elif score >= 80 and score <= 89:
    grade = "B"
elif score >= 70 and score <= 79:
    grade = "C"
elif score >= 60 and score <= 69:
    grade = "D"
elif score < 60:
    grade = "F"

print("Score: ", score, "         Grade: ", grade)



# Find and Fix the Mistakes
age = int(input("Enter your age: "))

if age == 18:
    print("Exactly Eighteen")
else:
    print("Good age")

score = 95
if score >= 90:
    grade = "A"
elif score >= 60:
    grade = "D"

print("Grade : ", grade)



# Build a Cinema Ticket Pricer
print("=" * 43)
print("         Dewa's Cinema Ticketing System")
print("=" * 43)

age = int(input("Enter your age         : "))
day = input("Enter day of the week  : ")

if age < 13:
    print("Ticket Price           : 5,000 Won")
    price = 5000
elif age >=13 and age <=64:
    print("Ticket Price           : 12,000 Won")
    price = 12000
else:
    print("Ticket Price           : 7,000 Won")
    price = 7000

if day == "Wednesday" or day == "wednesday":
    print("Discount              : 20%")
    if age < 13:
        print("Final Price            : ", price * 0.8, " Won")
    elif age >=13 and age <=64:
        print("Final Price            : ", price * 0.8, " Won")
    else:
        print("Final Price            : ", price * 0.8, " Won")



# Program that Ask for a number and print whether it is positive, negative or zero
num = int(input("Enter a number: "))

if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")



# Program that Ask for an age and print Child (under 13), Teenager (13–19) or Adult (20+)
age = int(input("Enter your age : "))

if age < 13:
    print("Child")
elif age >= 13 and age <= 19:
    print("Teenager")
else:
    print("Adult")
    


# Program that Ask for a year and report whether it is a leap year
year = int(input("Enter any year you like : "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year, "is a leap year")
        else:
            print(year, "is not a leap year")
    else:
        print(year, "is a leap year")
else:
    print(year, "is not a leap year")



# Ask for three test scores and print PASS only if all three are 60 or above
score1 = float(input("Enter the first score: "))
score2 = float(input("Enter the second score: "))
score3 = float(input("Enter the third score: "))

if score1 >= 60 and score2 >= 60 and score3 >= 60:
    print("Yeahhhhhhhhhhhh!!!")
    print("You passed the course!")
else:
    print("Don't worry, you can try again next semester.")


