###############################################
# E1: Find  the items smaller that 10 
###############################################
# numbers = [1,4,18,3,15,2]

# for num in numbers:
#     if num < 10:
#         print("Numbers < 10: ",num, end = " ")



###############################################
# E2:  Remove the duplicates
###############################################
# numbers = [1,4,18,3,15,2,1,18,4]

# final_list = []


# for num in numbers:
#     # check if the number NOT in the final list -> if not exist, then append it
#     if num not in final_list:
#         final_list.append(num)

# numbers.sort()
# final_list.sort()

# print(numbers) # original list
# print(final_list) # list without duplicates


###############################################
# E3: Get only the even numbers from the list
###############################################
# numbers = [1,4,18,3,15,2,1,18,4]

# for num in numbers:
#     if num%2 == 0:
#         print(num, end = " ")  # 4 18 2 18 4

###############################################
# E4: Get the matched items between the two lists -> common values between the two lists
###############################################
# numbers1 = [1,4,18,3,15,2,1,18,4]
# numbers2 = [69,1,15,3,7,90,10]

# common_numbers = []

# for num1 in numbers1:
    
#     # check if each number in the first list exists in the second list
#     if num1 in numbers2:  # 
#         common_numbers.append(num1)

# print(common_numbers)

###############################################
# E5: While + List 
###############################################

""" 
Enter your number : 5
Enter your number : -1
Enter your number : 3
Enter your number : 4
Enter your number : -2
......
Enter your number : 0   -> exit point

All numbers are : -2 -1 3 4 5
Sum of all numbers: ....
The Min number :  -2
The max numbers: 5

!!!!!!! Achtung Achtung::: sum(), min(), max()  sind nicht erlaubt!
"""

all_numbers = []

total = 0

while True:

    user_input = int(input("Enter a numbers: "))

    if user_input == 0:
        break  # exit point 

    all_numbers.append(user_input)
    total += user_input


# Sort the list
all_numbers.sort()  # aufsteigend

# Get the min and max via sorting
min_number = all_numbers[0]
max_number = all_numbers[-1]


# Outputsphase
print(f"All numbers: {all_numbers}")
print(f"Total: {total}")

print(f"Min: {min_number}")
print(f"Max: {max_number}")


# print(min(all_numbers))
# print(max(all_numbers))
# print(sum(all_numbers))


