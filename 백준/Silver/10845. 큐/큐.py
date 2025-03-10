import sys
from collections import deque

def push(queue, x):
    queue.append(x)

def pop(queue):
    print(queue.popleft() if queue else -1)

def size(queue):
    print(len(queue))

def empty(queue):
    print(1 if not queue else 0)

def front(queue):
    print(queue[0] if queue else -1)

def back(queue):
    print(queue[-1] if queue else -1)

def process_commands():
    queue = deque()
    input_data = sys.stdin.read().splitlines()  # 한 번에 입력 받기
    n = int(input_data[0])  # 첫 줄은 명령 개수
    
    for i in range(1, n + 1):  # 두 번째 줄부터 명령어 처리
        command = input_data[i].split()
        cmd = command[0]

        if cmd == "push":
            push(queue, int(command[1]))
        elif cmd == "pop":
            pop(queue)
        elif cmd == "size":
            size(queue)
        elif cmd == "empty":
            empty(queue)
        elif cmd == "front":
            front(queue)
        elif cmd == "back":
            back(queue)
    
if __name__ == "__main__":
    process_commands()
