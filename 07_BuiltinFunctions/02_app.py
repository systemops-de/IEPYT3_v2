# https://docs.python.org/3/library/functions.html

print(abs(-5))


# chr(Char  unicode) ---> the charachter itself
print(chr(65)) # A
print(chr(66)) # B


# ord()
print(ord("A")) # 65
print(ord("B")) # 66


# eval()
print(eval("1+2")) # 3
print(1+2)

course = "python"
print(eval("len(course)")) # 6

# print(eval(input("Enter your equation: ")))


# pow()
print(pow(10, 2)) # 100 = 10^2 = 10**2


# reversed()
numbers = [1,2,3,4,5]

for num in reversed(numbers):
    print(num)


# zip()
mylist1 = [1, 2, 3]
mylist2 = ["A", "B", "C"]

for num1, num2 in zip(mylist1, mylist2):
    print(num1, num2)
     
