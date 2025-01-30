N = int(input(""))
if N < 10:
    N *= 10 

original = N
count = 0

while True:
    first = N // 10       
    last = N % 10         
    N = (last * 10) + (first + last) % 10
    count += 1
    if N == original:
        print(count)
        break
