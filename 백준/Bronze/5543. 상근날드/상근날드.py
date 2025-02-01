s_price=int(input())
j_price=int(input())
h_price=int(input())
coke=int(input())
c=int(input())

burger=[s_price,j_price,h_price]
bev=[coke,c]

print(min(burger)+min(bev)-50)