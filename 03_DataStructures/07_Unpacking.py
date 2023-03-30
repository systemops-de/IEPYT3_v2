
###### Unpacking ---> With the order of the containers

# List / Tuple

numbers = [10, 20, 30]

num1 = numbers[0]
num2 = numbers[1]
num3 = numbers[2]

print(num1, num2, num3)

##################################################
#### Via Unpacking
numbers = [10, 20, 30]
num1, num2, num3 = numbers  # [10, 20, 30]

print(num1, num2, num3)



# *others: will have the rest items
numbers = [10, 20, 30, 40, 50,60,70,80,90,100]
num1, num2, num3, *others = numbers

print(num1, num2, num3, others)

##################################################

numbers = [10, 20, 30, 40, 50,60,70,80,90,100]

num1, num2, *others  , last_num = numbers

print(num1, num2, others, last_num) # 10 20 [30, 40, 50, 60, 70, 80, 90] 100



numbers = [10, 20, 30, 40, 50,60,70,80,90,100]

num1, *others , last_num = numbers

print(num1, others, last_num)



########################################################
# Example

x, y = (10, 20)
x, y = 10, 20

print(x, y)


#########################################
# Ebru Question 
numbers = [10, 20, 30, 40, 50,60,70,80,90,100]
a,b,c = numbers[0:3], numbers[4], numbers[5:]
print(a,b,c) # [10, 20, 30] 50 [60, 70, 80, 90, 100]
