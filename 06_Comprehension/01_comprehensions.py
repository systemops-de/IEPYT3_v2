""" 
Comprehension : Concise FORM  --> short cut --> compact expression
"""


numbers = [1, 2, 3, 4, 5]


# Normal way
# ~~~~~~~~~~~~++
squared_items = []
for num in numbers:
    squared_items.append(num * 2)

print(numbers)
print(squared_items)


# Short cut way
# ~~~~~~~~~~~~++
squared_items = [num * 2 for num in numbers]
print(squared_items)
print()

###############################################
numbers = [1, 2, 3, 4, 5]

# Normal way
even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

print(numbers)
print(even_numbers)


# Short cut way
# ~~~~~~~~~~~~++
even_numbers = [num for num in numbers if num % 2 == 0 ]

print(even_numbers)


###############################################
fruits = ["apple", "banana", "orange", "mango"]
output = ["Apple", "banana", "Orange", "mango"]

capitalized_fruits = []


# Normal way

for fruit in fruits:
    if fruit[0] in "aeoiuAEOIU":
        capitalized_fruits.append(fruit.title())
    else:
        capitalized_fruits.append(fruit)

print(capitalized_fruits)

# Short cut way
# ~~~~~~~~~~~~++

capitalized_fruits = [fruit.title() if fruit[0] in "aeoiuAEOIU" else fruit for fruit in fruits]


print(capitalized_fruits)
