import sys
N = int(input())
case = sys.stdin.read().splitlines()
for i in range(N):
    
    words = case[i].split()
    reversed_words = ' '.join(words[::-1])
    print(f'Case #{i+1}: {reversed_words}')