cart = []

while True:
    item = input("Enter item (or 'done' to finish): ")

    if item.lower() == "done":
        break

    cart.append(item)

print("\nItems in Cart:",cart)

 
