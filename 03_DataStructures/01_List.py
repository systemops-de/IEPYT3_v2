numbers = [1, 2, 3]
print(numbers, type(numbers)) # [1, 2, 3] <class 'list'>


teilnehmende = ["Thomas", "Ingo", "Sara", "Lena", "Julia", "Frank", "Mattias", "Sabine"]
print(teilnehmende)


mixed_data = [ "Thomas" , 55 , 12.3, True, ["VW", "Audi"]   ]
print(mixed_data, type(mixed_data))


matrix = [ [1, 2], [3, 4]]
print(matrix, type(matrix))


zeros = [0] * 20
print(zeros)


christoph_list = [ numbers ,  mixed_data ]
print(christoph_list)


# Add lists --> concatenate lists
mylist1 = [1,2,3]
mylist2 = ["A", "B", "C"]

total_list = mylist1 + mylist2
print(total_list)