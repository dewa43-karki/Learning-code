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



