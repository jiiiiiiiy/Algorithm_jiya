import sys

T = int(input())

for i in range(T):
    numbers = list(map(int, sys.stdin.readline().split()))  # 숫자 리스트 변환
    print(sum(numbers))
