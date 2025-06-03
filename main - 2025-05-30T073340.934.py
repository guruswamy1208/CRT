# Enter your code here
def solve(n):
    for i in range(n+1):
        for j in range(n-1):
            print(' ',end='')
            c=1
            for j in range(1,i+1):
            print(c,' ',sep='',end='')
            c=c*(i-j)//j 
        print()