
price = 123.456789

# 1. way
print(f"Price : {round(price, 2)}") # Price : 123.46

# 2. way
print(f"Price : {price:.1f}") # 123.5
print(f"Price : {price:.2f}") # 123.46

####################################

price = 1200
print(price)


price = 12e2
print(price)  # 1200.0

price = 1.2e2
print(price)  # 120.0

price = 12e-1
print(price)  # 1.2


price = 12e-2
print(price)  # 0.12

price = 12e-5
print(price)  # 0.00012



