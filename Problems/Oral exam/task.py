from collections import deque
n = int(input())
check_queue = deque()
complete_queue = deque()
for _i in range(n):
    record = input()
    if record.split()[0] == "READY":
        check_queue.appendleft(record.split()[1])
    if record == "EXTRA":
        check_queue.appendleft(check_queue.pop())
    if record == "PASSED":
        complete_queue.appendleft(check_queue.pop())

while len(complete_queue) > 0:
    print(complete_queue.pop())
