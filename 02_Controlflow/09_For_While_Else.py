temp = 30

if temp > 25:
    pass 

else:
    pass


##########################################################
for num in range(10):
    print(num)
    if num == 4:
        break        
else: # will be executed if there is no break, Exception
    print("The loop is normally finished")



##########################################################
temp = 30

while temp > 25:
    print("Temperature:", temp)
    temp -= 1  
    if temp == 28:
        break # will be executed if there is no break, Exception

else:
    print("The loop is normally finished")
