teilnehmende_list = ["Thomas", "Ingo", "Sara", "Lena", "Julia", "Frank", "Mattias", "Mattias", "Mattias", "Sabine"]
print(teilnehmende_list)

# Add new values
teilnehmende_list.append("Ario") ##-> am Ende
print(teilnehmende_list)

teilnehmende_list.append("Mario") ##-> am Ende
print(teilnehmende_list)



teilnehmende_list.insert(1, "Steffi") # insert into a certain index
print(teilnehmende_list)



# Edit value 
teilnehmende_list[1] = "Steffanie"
print(teilnehmende_list)



# Delete value
teilnehmende_list.pop()  # deletes the last item
print(teilnehmende_list)

teilnehmende_list.pop(2) # deletes a certain index
print(teilnehmende_list)

teilnehmende_list.remove("Mattias") # deletes the first match
print(teilnehmende_list)



##### Alternative
# Deletes single value
del teilnehmende_list[0]
print(teilnehmende_list)


# Deletes several values
del teilnehmende_list[0:5]
print(teilnehmende_list)


del teilnehmende_list

print("Ende")
