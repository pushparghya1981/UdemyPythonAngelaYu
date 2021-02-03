# Lists

grocery = ["Harpic", "Vim Bar", "deodorant", "Bhindi", "Chocolate", 78]
print(grocery)
print(grocery[4])

numbers = [2, 7, 9, 13, 16]
print(numbers)
print("List Size:", len(numbers))
print("List Max :", max(numbers))
print("List Min:", min(numbers))
print(numbers[3])

numbers.sort()
print("Sorted List:", numbers)

numbers.reverse()
print("Reversed List:", numbers)

# Slicing
print(numbers[1:len(numbers):2])

# adding items to list
numbers.append(45)
numbers.append(4)
numbers.append(33)
print("Numbers after append:", numbers)

# add item to list by index
numbers.insert(5, 101)
print("Insert at 5th index:", numbers)

# remove item from list
numbers.remove(101)
print("After remove item (101):", numbers)

# remove item from last
numbers.pop()
print("After pop:", numbers)
