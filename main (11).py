def factorial(n):
    if(n==0):
        return 1
    else:
        return n* factorial(n-1)
ans=factorial(6)
print(ans)