# the list "girls" is already defined
cute_girls = []
for _i, x in enumerate(girls):
    if x['education'] == "MIT" and x['about'] != "":
        cute_girls.append(x['name'])

print(", ".join(cute_girls))
