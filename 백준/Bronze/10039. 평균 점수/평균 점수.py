import sys
grades=list(map(int,sys.stdin.read().splitlines()))
for i in range(len(grades)):
    if grades[i] < 40:
        grades[i] = 40
print(sum(grades)//5)