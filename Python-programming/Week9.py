# Program that stores five students marks
mark1 = 78
mark2 = 92
mark3 = 65
mark4 = 88
mark5 = 71

total = mark1 + mark2 + mark3 + mark4 + mark5
print("Average: ", total / 5)



# Program for creating and reading a list
marks = [78, 92, 65, 88, 71]
names = ["Dewa", "Wadee", "Karki"]
mixed = ["Dewa", 19, True]
empty = []

print(marks[0])
print(marks[-1])
print(len(marks))

print(marks[1:4])



# Program that shows lists are mutable
marks = [78, 92, 65]
print(marks)

word = "Python"

marks.append(90)
print(marks)



# Program that adds and remove items
marks = [78, 92, 65]
print("Start: ", marks)

marks.append(88)
print("After append:", marks)

marks.insert(0, 100)
print("After insert:", marks)

marks.remove(65)
print("After remove:", marks)

last = marks.pop()
print("Popped:", last, "| List now:", marks)



# Program for looping through a list
marks = [78, 92, 65, 88, 71]

for mark in marks:
    print(mark)

total = 0
for mark in marks:
    total += mark
print("Total:", total)

passes = 0
for mark in marks:
    if mark >= 70:
        passes += 1

print("Passes:", passes)



# Program for getting positions too: enumerate()
names = ["Dewa", "Waadee", "Karki"]

for name in names:
    print(name)

for position, name in enumerate(names, start=1):
    print(position, "-", name)

print()
for i, item in enumerate(["Add", "View", "Exit"], start=1):
    print(f"{i}.{item}")



# Program that shows how built-in functions work on list
marks = [78, 92, 65, 88, 71]

print("How many     :", len(marks))
print("Highest      :", max(marks))
print("Lowest       :", min(marks))
print("Total        :", sum(marks))
print("Average      :", sum(marks)/ len(marks))

print("Sorted       :", sorted(marks))
print("Original     :", marks)

marks.sort()
print("After sort() :", marks)



# Program to see how tuple works as its immutable
point = (10, 20)
 
print(point[0])     
print(len(point))   
 
print(point)



# Program that takes several values out at once
def get_min_max(numbers):
    return min(numbers), max(numbers)

result = get_min_max([78, 92, 65])
print(result, type(result))

lowest, highest = get_min_max([78, 92, 65])
print("Lowest:", lowest, "| Highest:", highest)

a, b = 1, 2
a, b = b, a
print(a, b)



# Program that demonstrates aliasing trap
a = [1, 2, 3]
b = a                    
 
b.append(4)
print("b is", b)
print("a is", a)       
 
x = [1, 2, 3]
y = x.copy()          
 
y.append(4)
print("y is", y)
print("x is", x)



# Practise program of analysing a list of marks
marks = [78, 92, 65, 88, 71, 55, 94]

count = 0
for mark in marks:
    if mark >= 70:
        count += 1
print(f"Number of students who passed: {count}")

total = 0
for mark in marks:
    total += mark
print("Total :", total, "Average :", round(total / len(marks), 2))

print(f"Max marks: {max(marks)}, Min marks: {min(marks)}")

for position,  mark in enumerate(marks, start = 1):
    print(position, ".", mark)



# Practise Program to build a marks manager
marks = []

def add_mark(marks_list, value):
    marks_list.append(value)

def show_status(marks_list):
    if len(marks_list) == 0:
        print("No marks yet.")
        return
    total = sum(marks_list)
    print("Count :", len(marks_list), "Average :", round(total / len(marks_list), 2))
    print("Highest :", max(marks_list), "Lowest :", min(marks_list))

while True:
    print("1 = Add     2 = Stats     3 = Exit")
    choice = input("Choose: ")
    if choice == "1" :
       add_mark(marks, float(input("Mark : ")))
    elif choice == "2":
        show_status(marks)
    elif choice == "3" :
        print("ByeByeeeeee")
        break



