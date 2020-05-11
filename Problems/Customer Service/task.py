from collections import deque
request_number = int(input())
request_queue = deque()
for _i in range(request_number):
    request = input()
    if request.split()[0] == "ISSUE":
        request_queue.appendleft(request.split()[1])
    if request.split()[0] == "SOLVED":
        request_queue.pop()

while len(request_queue) > 0:
    print(request_queue.pop())
