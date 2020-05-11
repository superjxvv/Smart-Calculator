# the object_list has already been defined
# write your code here
from collections.abc import Hashable

output = 0
hash_values = dict()
for x in object_list:
    if isinstance(x, Hashable):
        if x in hash_values:
            hash_values[x] += 1
        else:
            hash_values[x] = 1

for x in hash_values:
    if hash_values[x] > 1:
        output += hash_values[x]

print(output)
