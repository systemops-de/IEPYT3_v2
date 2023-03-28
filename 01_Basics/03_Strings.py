# Define a string 
course_name = "Python"
course_name = 'Python'

print(course_name)


# Multi Line String 
message = """Hallo Sara,
wie geht es dir ?
schöne Grüße
Mohamed"""

print(message)



# Functions  len()
course_name = "Einführung in Python"
print(len(course_name)) # len: length

###############################################
# Slicing

course_name = "Einführung in Python"

print(course_name[0])
print(course_name[3])
print(course_name[19])
print(course_name[0:9]) # Einführun
print(course_name[0:10]) # Einführung
print(course_name[14:20]) # Python

# Python does not show out of range error
print(course_name[14:21]) # Python
print(course_name[14:100]) # Python
print(course_name[14:1000]) # Python


print(course_name[-20:-10]) # Einführung
print(course_name[-6:0]) # Empty 


print(course_name[14:]) # Python --> from 14 till the end
print(course_name[-6:]) # Python --> from -6 till the end

print(course_name[:10]) # Python --> from zero till 9
print(course_name[:]) # complete , from begining till the end
print(course_name) # complete

print()

#####################################################
# String methods -> DOT FUNCTION
course_name = "   einFühRunG iN pyTHoN  PyTHoN "
print(course_name)

# Gives me a new View (Ansicht) Version -> without changing the original container
print(course_name.upper())
print(course_name.lower())
print(course_name.title())
print(course_name.strip())
print(course_name.find("py")) # retrieve the index where 'py' starts
print(course_name.find("jy")) # -1 : not found

print(course_name.replace("py", "jy"))  # replace all 'py' in the text
print(course_name.replace("banana", "jy"))  # not found, nothing happend
print(course_name.count("py"))  # 1 


# To Change the original
course_name = course_name.strip()
course_name = course_name.title()
print(course_name)
print()

# Method Chain  --> from Left to right
course_name = "   einFühRunG iN pyTHoN  PyTHoN "
print(course_name) #    einFühRunG iN pyTHoN  PyTHoN

# overwrite the original variable with the new changed value
course_name = course_name.strip().title()
print(course_name) # Einführung In Python  Python
print()

##################################################
# String Concatenation
first_name = "Thomas"
last_name = "Meier"
print(first_name + last_name)


full_name = first_name + " " +  last_name
print(full_name)

####################################################
# String formatting -> To build a string content
first_name = "Sven"
last_name = "Meier"

full_name = "FN: {}  -  LN: {}".format(first_name, last_name)
print(full_name)

# Alternative
full_name = f"FN: {first_name}  -  LN: {last_name}"
print(full_name)

###################################################
# Escape/Ignore Charachter \
# \n: New Line   \t: TAB


# Mohamed sagte "Guten Morgen" heute !
# Mohamed sagte \Guten Morgen\ heute !

print("Mohamed sagte \"Guten Morgen\" heute !")
print('Mohamed sagte \'Guten Morgen\' heute !')
print('Mohamed sagte \\Guten Morgen\\ heute !')


print("Python\nJava")
print("Python\tJava")