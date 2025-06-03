# Enter your code here
arr=list(map(int,input().split()))
n=int(input())
count=0
for i in range(0,n):
    if(arr[i]%3==0):
        count=count+(arr[i]/3)
    elif(arr[i]%3!=0):
        count=count+(arr[i]//3)+1
print(int(count))    