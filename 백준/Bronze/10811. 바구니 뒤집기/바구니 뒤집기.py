N,M=map(int,input().split())
baguni=[]
for x in range(1,N+1):
    baguni.append(x)
for y in range(M):
    i,j=map(int,input().split())
    baguni[i-1:j]=baguni[i-1:j][::-1]
for items in baguni:
    print(items,sep=" ")