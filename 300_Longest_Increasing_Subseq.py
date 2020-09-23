'''
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
'''
# DP - TC: O(n^2) SC: O(n)

class Solution:
    def lengthOfLIS(self, nums):
        if not nums:
            return 0

        dp = [1 for i in range(len(nums))]

        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i],dp[j]+1)

        return max(dp)

#  DP & Binary Search- TC: O(nlogn) SC: O(n)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        def helper(res, left, right, target):
            while left < right - 1:
                mid = (left + right) // 2
                if res[mid] >= target:
                    right = mid
                else:
                    left = mid
            return right
        
        if not nums:
            return 0
        
        res = [nums[0]]
        for i in range(len(nums)):
            if nums[i] <= res[0]:
                res[0] = nums[i]
            elif nums[i] > res[-1]:
                res.append(nums[i])
            else:
                idx = helper(res, 0, len(res), nums[i])
                res[idx] = min(nums[i], res[idx])
        
        return len(res)
    

# same as above with inbuilt fn for binary search

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = []
        for num in nums:
            i = bisect.bisect_left(res, num)
            if i >= len(res):
                res.append(num)
            else:
                res[i] = num
        return len(res)
