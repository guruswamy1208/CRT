# Enter your code here bubble sort guru swamy
def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
        
arr=[9,3,4,6,8,2]
result=bubble_sort(arr)
print(result)