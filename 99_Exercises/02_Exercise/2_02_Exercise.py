# Online Shop

""" 
Conditions:
~~~~~~~~~~~~
- age : >= 18
- payment_method : True
- items: Product count > 0  -> warenkorb



# Exercise 1: 
- Show signle message of the missing condition

# Exercise 2: 
- Show ALLLLL Messages of ALLL Missing conditions


# Messages:
- Du bist zu jung
- BZ Methode nicht vorhanden
- Du muss Produkte auswählen
+ Zur Kasse bitte

"""


# Start Code
age = 17  
payment_method  = True 
items = 1



# Your code
################################################################################
# Exercise 1: 
# Show signle message of the missing condition
################################################################################

# if age >=18:
#     if payment_method == True:
#         if items > 0:
#             # Best case
#             print("Zur Kasse bitte")

#         else:
#             print("Du muss Produkte auswählen") 
#     else:
#         print("BZ Methode nicht vorhanden") 
# else:
#     print("Du bist zu jung")

################################################################################
################################################################################
# Exercise 2: 
# Show ALLLLL Messages of ALLL Missing conditions
################################################################################

age = 17  
payment_method  = True 
items = 1
customer_card = 1

# if age>=18 and payment_method==True and items >0: # best case
#     print("Zur Kasse bitte")

# elif age<18 and payment_method==True and items >0:
#     print("Du bist zu jung")

# elif age>=18 and payment_method==False and items >0:
#     print("BZ Methode nicht vorhanden")

# elif age>=18 and payment_method==True and items < 1:
#     print("Du muss Produkte auswählen")
# else:  ## all other combinations should be written
#     pass 



################################################################################
# Exercise 2: - Solution 1
# Show ALLLLL Messages of ALLL Missing conditions
################################################################################

age = 27  
payment_method  = True 
items = 2

# # Best case

# if age >= 18 and payment_method == True and items > 0:
#     print("Zur Kasse bitte")

# else:

#     if age < 18:
#         print("Du bist zu jung")

#     if payment_method == False:
#         print("BZ Methode nicht vorhanden")

#     if items < 1:
#         print("Du muss Produkte auswählen")


################################################################################
# Exercise 2: - Solution 2
# Show ALLLLL Messages of ALLL Missing conditions
################################################################################

age = 27  
payment_method  = True 
items = 1
customer_card = False


all_crit_valid = True  # Flag - Helping variable


if age < 18:
    print("Du bist zu jung")
    all_crit_valid = False
    
if payment_method == False: #FIXME: don'T compare, use bool not
    print("BZ Methode nicht vorhanden")
    all_crit_valid = False

if customer_card == False:
    print("Du muss Kundenkarte haben")
    all_crit_valid = False

if items < 1:
    print("Du muss Produkte auswählen")
    all_crit_valid = False

if all_crit_valid == True: # FIXME: use bool directly
    print("Zur Kasse bitte")


