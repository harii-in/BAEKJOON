from queue import PriorityQueue
import sys
input = sys.stdin.readline

N = int(input())
queue = PriorityQueue()

for _ in range(N):
    x = int(input())

    if x != 0:
        queue.put((abs(x), x))
    else:
        if queue.empty():
            print(0)
        else:
            print(queue.get()[1])
