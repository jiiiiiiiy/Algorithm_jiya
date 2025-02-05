import sys

N = int(sys.stdin.readline().strip())  # 빠른 입력
stack = []
commands = sys.stdin.read().splitlines()  # 한 번에 입력 받기

for command in commands:
    order_list = command.split()
    order = order_list[0]

    if order == '1':
        stack.append(order_list[1])
    elif order == '2':
        print(-1 if not stack else stack.pop())
    elif order == '3':
        print(len(stack))
    elif order == '4':
        print(1 if not stack else 0)
    elif order == '5':
        print(-1 if not stack else stack[-1])
