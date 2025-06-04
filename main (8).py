def natural(n):
    if(n==0):
        return 1
    else:
        print(n,end=" ")
        return natural(n-1)
ans=natural(5)
print(ans)