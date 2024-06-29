#problem 1991 leetcode
# 1991. Find the Middle Index in Array
class Solution:
    def findMiddleIndex(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        
        for i in range(1, n):
            nums[i] += nums[i-1]
        print(nums)
        
        for i in range(n):
            kiri = nums[i-1] if i > 0 else 0
            kanan = nums[-1] - nums[i]
            print(kiri, kanan)
            if kiri == kanan:
                return i
        return -1
    
# Test the function
nums = [2, 3, -1, 8, 4]
print(Solution().findMiddleIndex(nums))  # Output: 3
nums = [1, -1, 4]
print(Solution().findMiddleIndex(nums))  # Output: 2
nums = [2, 5]
print(Solution().findMiddleIndex(nums))  # Output: -1