# Program that stores student and their marks with a list, showcasing why dictionaries
names = ["Dewa", "Karki", "Waadee"]
marks = [99, 87, 91]

position = names.index("Dewa")
print("Dewa's Mark: ", marks[position])



# Program for creating and reading a dictionary
marks = {"Dewa": 99, "Waadeee": 94, "Karki": 100}

print(marks)
print(len(marks))

print(marks["Waadeee"])

print(marks.get("ARKI"))
print(marks.get("ARKI", 0))



# Program for changing a Dictionary
marks = {"Dewa": 98, "Karki": 100}

marks["Waaadee"] = 95
print(marks)

marks["Dewa"] = 100
print(marks)

del marks["Karki"]
print(marks)



# Program to see how loops works for Dictionary
marks = {"Dewa": 98, "Karki": 100, "Waadee": 95}

for name in marks:
    print(name)

for mark in marks.values():
    print(mark)

for name, mark in marks.items():
    print(f"{name}: {mark}")

print("Average:", sum(marks.values()) / len(marks))



  # Program to count how often things appear   - Practical Example
sentence = input("Enter a sentence: ")
words = sentence.lower().split()

counts = {}

for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

for word, number in counts.items():
    print(f"{word}: {number}")



# Program to show the importance of a sets
marks = [99, 88, 94, 100, 97, 99, 94, 88]

unique = []
for mark in marks:
    if mark not in unique:
        unique.append(mark)

print(unique)



# Program for creating and using a set 
marks = [99, 88, 94, 100, 97]

unique = set(marks)
print(unique)
print("How many unique:", len(unique))

color = {"Red", "Green", "Blue", "Black"}
color.add("Black")
color.add("Grey")
print(color)

print("Red" in color)

empty = set()



# Program to compare two sets
python_class = {"Dewa", "Karki", "Waadee"}
maths_class = {"Dewa", "Waadee", "Arki", "Ari"}

print(python_class & maths_class)

print(python_class | maths_class)

print(python_class - maths_class)

print(python_class.intersection(maths_class))



# Program for  one problem, and four way structure which fits it the best
attendence = ["Dewa", "Waadee", "Arki", "Ari"]
print("Total check-ins:", len(attendence))

print("Unique students:", len(set(attendence)))

marks = {"Dewaa": 99, "Karkii": 100, "Waadee": 95}
print("Dewa scored:", marks["Dewaa"])

exam_dates = ("2026-11-10", "2026-11-22")
print("First exam:", exam_dates[0])



# Program that has 2 list with students name, and print who is in both and who is only in one
names1 = ["Dewa", "Sachh", "Jenn", "J", "Dragonsbaene", "Karki"]
names2 = ["Dragonsbaene", "Waadee", "C3PO", "R2D2", "Arkii"]

def names():
    for name in names1 and names2:
        if names1 == names2:
            print("These belongs in both the list :", names)
        if names1 != names2:
            print("These are not in the same group: ", names)
        
names()



# Program that takes a list with duplicates and print its unique value using a set
items = [1, 2, 3, 4, 4, 3, 3, 3, 4, 5]
unique_items = set(items)

print(unique_items)



# Program to count the letters in a word using a dictionaryyy
word = "banana"
letter_counts = {}

for letter in word.lower():
    if letter.isalpha():
        letter_counts[letter] = letter_counts.get(letter, 0) + 1

print(letter_counts)



# Program to build a phone book
contacts = {}

def add_contact(book, name, number):
    book[name] = number

def find_contact(book, name):
    return book.get(name, "Not Found")

def show_all(book):
    for name, number in book.items():
        print(f"{name} : {number}")

    if len(book) == 0:
        print("Phone book is empty")
        return

while True:
    print("1 = Add,  2 = Find,  3 = Show All,  4 = Exit")
    choice = int(input("Choose : "))

    if choice == 1:
        n = input("Name      : ")
        nub = int(input("Number   : "))
        add_contact(contacts, n, nub)
    elif choice == 2:
        print(find_contact(contacts, input("Name: ")))
    elif choice == 3:
        show_all(contacts)
    elif choice == 4:
        break


