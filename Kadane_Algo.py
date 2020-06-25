#fastest
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m = nums[0]
        tempm = nums[0]
        for i in nums[1:]:
            if i > tempm and tempm < 0:
                tempm = i
            else:
                tempm += i            
            if tempm > m:
                m = tempm     
        return m
        
        
#lightest
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxNum = nums[0]
        acc = nums[0]
        for n in nums[1:]:
            acc += n
            maxNum = max(acc, maxNum, n)
            if n > acc:
                acc = n
        return maxNum
