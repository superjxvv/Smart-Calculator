# put your python code here
from collections import deque

stack = deque()
string = input()
try:
    for i in string:
        if i == "(":
            stack.append(i)
        if i == ")":
            stack.pop()
except IndexError:
    print("ERROR")
else:
    if len(stack) > 0:
        print("ERROR")
    else:
        print("OK")
