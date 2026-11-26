# Program to extracting parts of a string
word = "PROGRAMMING"

print(word[0:3])
print(word[3:7])

print(word[:4])
print(word[7:])
print(word[:])

print(word[-4:])

student_id = "2026CS081"
print("Year   :", student_id[:4])
print("Course :", student_id[4:6])



# Program for a for loop that can visit each character in turn
word = input("Enter a word: ")

for letter in word:
    print(letter)

vowel_count = 0

for letter in word:
    if letter.lower() in "aeiou":
        vowel_count += 1

print(word, "has", vowel_count, "vowels")



# Program to see immutable in python - trying to change a string
word = "Dewadd"

new_word = "S" + word[1:]
print(new_word)
print(word)



# Program to change word case of a string
name = "KaRKi DeWA"

print(name.upper())
print(name.lower())
print(name.title())
print(name.capitalize())

print(name)

name = name.title()
print(name)



# Program for tidying input and finding things inside a text
messy = "     KTM, Nepal   "

print("[" + messy.strip() + "]")

text = "Python is fun and Python is powerful"

print(text.count("Python"))
print(text.find("fun"))
print(text.replace("Python", "Coding"))

print("Python" in text)

print(text.startswith("Python"))
print(text.endswith("!"))



# Program that turns a sentence into pieces and pieces back into a sentence
sentence = "Python is really fun."

words = sentence.split()
print(words)
print("Word count: ", len(words))

data = "2026,CS-404,Dewa"
parts = data.split(",")
print(parts)
print("Name:", parts[2])

print(" ".join(words))
print("-".join(parts))



# Program that builds a cleaner text containing variable values
name = "Dewa"
score = 95.5

print("Name:", name, "Score:", score)

print(f"Name: {name}, Score: {score}")

print(f"Score: {score: .2f}")
print(f"Name: {name:>12}")
print(f"Doubled: {score * 2:.1f}")


# Program that checks a password for length, digits and spaces
print("=" * 44)
print("              Password Checker                ")
print("=" * 44)

password = input("Enter a password: ")

long_enough = len(password) >= 8

digits = 0
for digit in password:
    if digit.isdigit():
        digits += 1

has_digit = digits >= 1
no_spaces = " " not in password

accepted = long_enough and has_digit and no_spaces

print(f"Length OK : {long_enough}")
print(f"Has digit  : {has_digit}")
print(f"No spaces  : {no_spaces}")  
print(f"Password accepted: {accepted}")



# Program that ask for full name and then print the iniitals
full_name = input("Enter your full name: ")

name = full_name.split()  

initials = [word[0].upper() for word in name]

result = " ".join(initials)

print(f"The initials are: {result}")



# Program that ask for a word and then print it backwards
words = input("Enter a word: ")

backwards = words[::-1]
print(f"The word backwards is: {backwards}")

words = words.split()
reversed_words = words[::-1]
output = " ".join(reversed_words)
print(f"The words backwards are: {output}")



# Program that returns if a word is a palindrome or not using function
def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]

word = input("Enter a word: ")
if is_palindrome(word):
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")



# Program that asks for a sentence and print how many words are longer than four letters
sentence = input("Enter a sentence: ")
words = sentence.split()
count = 0

for word in words:
    if len(word) > 4:
        count += 1

print(f"Number of words longer than four letters: {count}")

