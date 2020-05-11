from collections import deque

n = int(input())

my_stack = deque()

for _i in range(n):
    my_stack.append(input())

for _i in range(n):
    print(my_stack.pop())
