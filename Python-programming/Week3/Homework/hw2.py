price = float(input("Enter the price of Jhol Momo: "))
quantity = int(input("Enter the quantity            : "))

amount = price * quantity
discount = amount * 0.1 

print("The total amount after 10% discount is ", amount - discount)
