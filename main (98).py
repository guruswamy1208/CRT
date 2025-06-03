# Enter your code here
def insertion_sort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -=1
        arr[j+1]=key
    return arr
arr=[9,3,4,6,8,2]
insertion_sort=arr
print(insertion_sort)