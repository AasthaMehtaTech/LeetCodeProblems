'''
Example 1:

Input: [1,3,4,2,2]
Output: 2
Example 2:

Input: [3,3,3,4,2]
Output: 3
'''
# 1 - Sort & search : TC: O(nlgn), SC: O(1), O(n)- if in place sort not permitted
# 2 - Iterate every element & add it in set - TC: O(n) , SC: O(n)
# 3 - Floyd's Algo - TC: O(n), SC: O(1)

#fastest 
from collections import defaultdict
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dict = defaultdict(int)
        for n in nums:
            dict[n] += 1
            if dict[n] > 1: return n
            
#https://leetcode.com/problems/find-the-duplicate-number/solution/

#Floyd's Circular Loop Detection

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = ans = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        while ans != slow:
            ans = nums[ans]
            slow = nums[slow]
        return ans
