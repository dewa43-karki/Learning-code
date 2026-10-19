# Program to see now range works
for i in range(1, 21):
    print(i)

print("Loop is finished.")


for i in range(2, 22, 2):
    print(i)
print("Loop is finished.")


word = input("Enter any word: ")
count1 = 0
for letter in word:
    count1 = count1 + 1

print("The number in that word is ", count1)


    
# Practice: Keep Asking Until Valid
number = int(input("Enter a number(1-10): "))
while number < 1 or number > 10:
    print("That is not between 1 and 10. Try again.")
    number = int(input("Enter a number (1-10): "))   
 
print("Thank you. You entered:", number)



# Practice: Running Total Until Zero
print("Enter numbers to add. Enter 0 to finish.")
 
total = 0                         
count = 0                          
value = float(input("Number: "))   
 
while value != 0:                 
    total += value
    count += 1
    value = float(input("Number: "))  
 
print("You entered", count, "numbers")
print("Total  :", total)
if count > 0:                     
    print("Average:", total / count)



# Program that print even number from 1-20
for i in range(2, 22, 2):
    print(i)
print("done")



# Program for break
for i in range(1, 6):
    if i == 3:
        break
    print(i)
 


# Practice: Multiplication Grid
print("Multiplication table 1 to 5")
print()
 
for row in range(1, 6):           
    for col in range(1, 6):       
        product = row * col
        print(f"{product:4}", end="")
    print()                        



# Program that count down from 10 to 1, then print "Done"
i = 10
while i in range(10, 0, -1):
    print(i)
    i -= 1
print("Done")



# Program that Keep asking for a password until the user types "python"
password = input("Enter your password: ")
while password != "python":
    print("Incorrect password. Try again.")
    password = input("Enter your password: ")
print("Access granted.")



# Program that start at 1 and keep adding 3 until the value passes 50, printing each value
i = 1
while i <= 50:
    print(i)
    i += 3



# Program that prints the multiplication table from 1-10
print("        Multiplication table       ")

for i in range (1, 11):
    for j in range(1,11):
        print(f"{i} x {j} = {j * i}")
    print()
        
        

# Practice: Number Guessing Game
secret = 7 

attempts = 0

print("Guess my number between 1 and 10!")

while True: 
    guess = int(input("Your guess: "))
    attempts += 1 # count this attempt
    if guess < secret:
        print("Too low. Try again.")
    elif guess > secret:
        print("Too high. Try again.")
    else:
        print("Correct! You took", attempts, "attempts.")
        break



# Program that take input till the user says yes and then find those numbers' average
count = 0
value = "yes"
total = 0

while value == "yes" :
    number = int(input("Enter the number: "))
    total += number
    count += 1
    value = input("Do you wanna continue? ")


average = total / count
print(average)



# The Simplest Nested Loop
for outer in range(1, 4):          
    for inner in range(1, 3):     
        print("outer =", outer, "| inner =", inner)
    print("--- end of outer round", outer, "---")



# Program that print the numbers 1 to 20, skipping any multiple of 3, using continue
for i in range(1, 21):
    if i % 3 == 0:
        continue
    print(i)



# Program that ask for numbers repeatedly and stop when the user enters a negative one, using break  
while True:
    num = int(input("Enter a number: "))
    if num < 0:
        break



# Program to use nested loops to print a 4 × 4 square of hash symbols
for i in range(4, 5, 4):
    for j in range(i):
        print("#" * i)
    print()

