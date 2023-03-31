

""" 
num1 &= num2  ---->  num1 = num1 & num2  : and
num1 |= num2  ---->  num1 = num1 | num2  : or
num1 ^= num2  ---->  num1 = num1 ^ num2  : xor
~num1         ---->  num1 = ~num2  : not     --->   ~num1 = -(1+num1)

a <<= b --->   a = a << b : bitwise left shifting
a >>= b --->   a = a >> b : bitwise right shifting

"""


num1 = 4
num2 = 10 

print("Num1 & Num2: ",  num1 & num2)  # and
print("Num1 | Num2: ",  num1 | num2)  # or
print("Num1 ^ Num2: ",  num1 ^ num2)  # and
print("~Num1 : ",  ~num1)  # not


result = num2 << 2 
print("10 << 2:  ", result)

result = 40 >> 3
print("40 >> 3:  ", result)