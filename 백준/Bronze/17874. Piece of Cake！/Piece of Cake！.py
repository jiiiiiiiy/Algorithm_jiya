n,h,v=map(int,input().split())
h_g=max(h,n-h)
v_g=max(v,n-v)
print(h_g*v_g*4)