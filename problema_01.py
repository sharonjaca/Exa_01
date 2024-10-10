# -----------------------------------
# declaring local arrayList
# -----------------------------------
vec1 = [5, 1, 7, 4, 9]
vec2 = [6, 8, 2, 5, 4, 3, 1]

# -----------------------------------
# Declaring join functions
# -----------------------------------

# Inner Join
def Join():
    salida = []
    for act in vec1:
     control = act in vec2
     if control:
            salida.append(act)
    return salida

# Full Join
def FullJoin():
    salida2 = vec1[:]
    for act in vec2:
     control = act in salida2
     if not control:
        salida2.append(act)
        return salida2

# Full Outer Join
def FullOuterJoin():
    salida = []
    for act in vec1:
     control = act in vec2
     if control:
            salida.append(act)
    for act in vec2:
          control = act in vec1
          if not control:
            salida.append(act)
            return salida

# Right Join
def RightJoin():
    salida = []
    for act in vec2:
        if act in vec1 or act not in vec1:
            salida.append(act)
    return salida

# -----------------------------------
# Executing join functions
# -----------------------------------
print("Inner Join :", Join())
print('')
print("Full Join :", FullJoin())
print('')
print("Full Outer Join :", FullOuterJoin())
print('')
print("Right Join :", RightJoin())
