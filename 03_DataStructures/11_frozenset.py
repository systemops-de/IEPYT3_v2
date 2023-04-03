"""
set() : you can add and remove items (mutable)
frozenset() : you cannot add new items

but you still can use the nice methods : union, intersection , etc.

"""

numbers1 = frozenset([1, 2, 3, 4, 5, 5, 5])
numbers2 = frozenset([4, 5, 10, 20, 30])

# frozenset({1, 2, 3, 4, 5}) <class 'frozenset'>
print(numbers1, type(numbers1))

print(numbers1.union(numbers2))  # frozenset({1, 2, 3, 4, 5, 10, 20, 30})

print(numbers1.intersection(numbers2))  # frozenset({4, 5})


# a- b : frozenset({1, 2, 3, 4, 5, 10, 20, 30})
print(numbers1.difference(numbers2))  # frozenset({1, 2, 3})
