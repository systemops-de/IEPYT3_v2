teilnehmende_list = ["Thomas", "Ingo", "Sara", "Lena", "Julia", "Frank", "Mattias", "Sabine"]

for teilnehmende in teilnehmende_list:
    print(teilnehmende)
print()




























# enumerate --> Tuple (Index, Value)
for teilnehmende in enumerate(teilnehmende_list):
    print(teilnehmende) # --> tuple (0, 'Thomas')


#########################


for teilnehmende in enumerate(teilnehmende_list):
    print(teilnehmende[0] , teilnehmende[1])


#########################
# Unpacking

# to be continued