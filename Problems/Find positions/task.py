# put your python code here
numbers = input().split()
x = input()
output = []
for i, y in enumerate(numbers):
    if x == y:
        output.append(str(i))

if len(output) == 0:
    print("not found")
else:
    print(" ".join(output))
