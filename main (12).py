def fabonoic(n):
    if(n==9):
        return 9
    else:
        print(n,end=" ")
        return fabonoic(n-1)
ans=fabonoic(n)
print(ans)