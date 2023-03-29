#################################################################
# E1: Sum of all numbers between 10 and 20 
#################################################################

# total = 0
# for num in range(10, 21):
#     total += num 

# print(f"Total : {total}")






#################################################################
# E2: Sum of all numbers between (lower_limit) and (upper_limit)
#################################################################

# lower_limit = int(input("Enter lower limit:"))  # 2   
# upper_limit = int(input("Enter upper limit:"))  # 5   

# total = 0
# for num in range(lower_limit, upper_limit + 1):
#     total += num 

# print(f"Total : {total}")



#################################################################
# E3: Get 5xnumbers from the user --> 
#################################################################

""" 
Enter your number : 5
Enter your number : -1
Enter your number : 3
Enter your number : 4
Enter your number : -2


All numbers are : 5 -1 3 4 -2
All pos. numbers are:  5 3 4
All neg. numbers are: -1 -2
"""

all_numbers = ""
pos_numbers = ""
neg_numbers = ""

 
for x in range(5):  
    user_input = int(input("Enter a number: "))
  
    all_numbers = f"{all_numbers} {user_input}"  #  # all_numbers += str(user_input) + " "    #  1  2   3   4  5 

    if user_input > 0: # positive number
        pos_numbers = f"{pos_numbers} {user_input}"

    elif user_input < 0: # negative number
        neg_numbers = f"{neg_numbers} {user_input}"


print(f"All numbers: {all_numbers}")
print(f"Pos numbers: {pos_numbers}")
print(f"Neg numbers: {neg_numbers}")
