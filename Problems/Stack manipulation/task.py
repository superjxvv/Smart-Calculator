from collections import deque

n = int(input())

stack = deque()
i = 0

while i < n:
    command = input().lower().split()
    if len(command) == 2:
        stack.append(command[1])
    elif len(command) == 1:
        stack.pop()
    i += 1

while len(stack) > 0:
    print(stack.pop())
