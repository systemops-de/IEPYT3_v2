teilnehmende = ["Thomas", "Ingo", "Sara", "Lena", "Julia", "Frank", "Mattias", "Sabine"]

print(teilnehmende)
print(teilnehmende[0])
print(teilnehmende[2])
print(teilnehmende[-1])
print(teilnehmende[7])
print(teilnehmende[1:5]) # ['Ingo', 'Sara', 'Lena', 'Julia']
print(teilnehmende[1 : 7 : 2 ]) # 


print()
#############################################################
user = ["Thomas", 55, 36.9 , ["Julia", "Frank"] ]

print(user[0], type(user[0]))
print(user[2], type(user[2]))
print(user[3], type(user[3]))


print(user[3]) # Kinderliste

print(user[3][0])
print()

#################################################
tn_liste = [
                ["Thomas", 55, ["Julia", "Lena", ["A", ["B"]]]],
                ["Ingo", 40, ["Marc"]],
                ["Frank", 27],
            ]

print(tn_liste[0][2][0]) # Julia
print(tn_liste[1][1]) # 40
print(tn_liste[1][2][0]) # Marc
print(tn_liste[2][1]) # 27
print(tn_liste[2][-1]) # 27
print(tn_liste[1][2][-1]) # Marc
print(tn_liste[-2][-1][-1]) # Marc
print(tn_liste[0][-1][-1][-1][-1]) # B
print(tn_liste[0][2][2][1][0]) # B