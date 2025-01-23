N,M=map(int,input().split())
matrix1=[]
matrix2=[]
for i in range(N):
    column=list(map(int,input().split()))
    matrix1.append(column)
for j in range(N):
    column=list(map(int,input().split()))
    matrix2.append(column)

matrix_sum=[]
for j in range(N):
    matrix=[]
    for i in range(M):
        matrix.append(matrix1[j][i]+matrix2[j][i])
    matrix_sum.append(matrix)
 
for items in matrix_sum:
    for item in items:
        print(item,end=" ")
    print()     