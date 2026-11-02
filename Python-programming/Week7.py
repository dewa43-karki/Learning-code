# Program to know the numeric built-ins
print(abs(-15))
print(round(3.7))
print(round(3.14149, 2))
print(min(4, 9, 2))
print(max(4, 9, 2))
print(pow(2, 10))

score = [78, 92, 65]
print(min(score), max(score), sum(score))
print(sum(score)/ len(score))



# Program that change or examine what a value is
print(int("42"), float("3.5"), str(99))
print(int(7.9))

print(type(42))
print(len("Python"))

print(bool(0), bool(5))
print(bool(""), bool("a"))



# Program to see how new built-in function works
print(dict(enumerate("Homework"))) 

print([bin(ord(char)) for char in "Dewa"])

print(divmod(45, 5))

print(repr("HIEEE"))

print(set("House"))



#Program that shows the difference between writing code and using built-in
def largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
 
print(largest(4, 9, 2))
 
print()
print(max(4, 9, 2))
 


# Program of a math module
import math

print(math.sqrt(64))
print(math.pi)
print(math.floor(4.8))
print(math.ceil(4.2))
print(math.pow(2,5))

radius = float(input("Enter the radius: "))
area = math.pi * radius ** 2
print("Area:", round(area, 2))



# Program that produce random using random module
import random

print(random.randint(1, 6))
print(random.random())
print(random.choice(["rock", "paper", "scissors"]))

for i in range(5):
    print(random.randint(1,6), end=" ")



# Practising to make a dice game
import random

print("--- DICE GAME ---")

wins = 0

for round_numbers in range(1, 6):
    player = random.randint(1, 6)
    computer = random.randint(1, 6)
    print("Round", round_numbers, "- you:", player, "computer:", computer)

    if player > computer:
        print("  YOUU ARE THE WORLD CHAMPION, A WORLD CHAMPION!!!")
        wins += 1
    elif player < computer:
        print("Well I hate to break it to you daddy, BUT YOU LOOOSE!!!")
    else: 
        print("Nice meeting an worth opponent!!!")

print("You won", wins, "times")



# Program to show a datetime module
import datetime

today = datetime.date.today()
print("Today is: ", today)

print("Year : ", today.year)
print("Month: ", today.month)
print("Day  : ", today.day)

birth_year = int(input("Enter your birth year: "))
age = today.year - birth_year
print("You are about", age, "years old")



# Practising the built-in function
a = -17
b = 3.86214

print(abs(a))

print(round(b, 2))

numbers = [45, 12,78, 33]
print(max(numbers), min(numbers))

print(type(a), type(b))

words = input("Enter any numbers: ")
print(words, "has", len(words), "letters")



# Practising a math quiz game
import random

def ask_question():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    sum = float(input(f"Sum of {a} + {b} is: "))

    if sum == a + b:
        print("Smart is the new sexyyy!")
        return True
    else:
        print("Life can't be more Bazinggaaa!")
        return False

score =  0
for i in range(5):
    if ask_question():
        score += 1

print("Score:", score, "of 5", " (" + str(score / 5 * 100) + "%)")



# Program for making a scissor-paper-rock game
import random

print("         Scissor-Paper-Rock       ")
wins = 0

for round_num in range(5):
    player = random.choice(["scissor", "paper", "rock"])
    computer = random.choice(["scissor", "paper", "rock"])
    print("Round", round_num, "-you:", player, "computer:", computer)

    if player > computer:
            print("  YOUU ARE THE WORLD CHAMPION, A WORLD CHAMPION!!!")
            wins += 1
    elif player < computer:
        print("Well I hate to break it to you daddy, BUT YOU LOOOSE!!!")
    else: 
        print("Nice meeting an worth opponent!!!")
    
print("You won", wins, "times")
