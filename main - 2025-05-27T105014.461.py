# Enter your code here 2nd question guru
r=int(input())
units=int(input())
n=int(input())
arr=list(map(int,input().split()))
food_required=r*units
if(len(arr)==0):
    print(-1)
for i in range(n):
    food_required=food_required-arr[i]
    if(food_required<0):

        break
if(food_required>0):
    print(0)
print(abs(food_required))

