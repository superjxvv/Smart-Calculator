# please, work with the variables 'Belov', 'Smith', and 'Sarada'
# Belov = ["Physics", "Math", "Russian"]
# Smith = ["Math", "Geometry", "English"]
# Sarada = ["Japanese", "Math", "Physics"]
# print(set(Belov + Smith + Sarada))
x = set(Belov).union(Smith).union(Sarada)
print(len(x))
