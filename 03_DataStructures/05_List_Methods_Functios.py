numbers = [40, 12, 1204, 1432,122, 1]
print(numbers)

###############################
# .sort() : changes its original container
numbers.sort() # aufsteigend
print(numbers)


numbers.sort(reverse= True)  # absteigend
print(numbers)


################################
# .count() : count of certain value
teilnehmende_list = ["Thomas", "Ingo", "Ingo", "Lena"]

print(teilnehmende_list.count("Ingo"))


###############################
# in --> to check if a value in a list or not
teilnehmende_list = ["Thomas", "Ingo", "Ingo", "Lena"]

if "Thomas" in teilnehmende_list:
    print("Thomas is da")
else:
    print("Thomas ist nicht da")


if "Thomas" not in teilnehmende_list:
    print("Thomas ist nicht da")
else:
    print("Thomas is da")


####################################
# Functions with Lists , etc.
####################################
teilnehmende_list = ["Thomas", "Ingo", "Ingo", "Lena"]
numbers = [40, 12, 1204, 1432,122, 1]


print(len(teilnehmende_list)) # 4 values
print(min(numbers))
print(max(numbers))
print(sum(numbers))


# sorted() : --> gives a NEW sorted list back, without changing the orignal one
mysorted = sorted(numbers)
print("Original: ", numbers)
print("Sorted: ", mysorted)


mysorted = sorted(numbers, reverse= True) # absteigend sortiert
print("Original: ", numbers)
print("Sorted Reversed: ", mysorted)






