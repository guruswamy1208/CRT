# Enter your code here
class Solution:
    def rotateNums(self, arr, k):
        #Your code here
        n=len(nums)
        temp=[0]*n
        k=k%n
        for i in range(len(nums)):
            temp[(i+k)%n]=nums[i]
            
        for i in range(len(nums)):
            nums[i]=temp[i]
        
        return nums
nums=[1,2,3,4,5,6,7]
k=2
print(Solution().rotateNums(nums,k))