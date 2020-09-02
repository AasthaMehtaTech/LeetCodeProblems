'''
  Given an array of integers, find out whether there are two distinct indices i and j in the array
  such that the absolute difference between nums[i] and nums[j] is at most t 
  and the absolute difference between i and j is at most k.
'''

# Sorted List (O (n*logk) ) : https://leetcode.com/problems/contains-duplicate-iii/discuss/824603/Python-SortedList-O(n-log-k)-solution-explained.

from sortedcontainers import SortedList

class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        SList = SortedList()
        for i in range(len(nums)):
            if i > k: SList.remove(nums[i-k-1])   
            pos1 = bisect_left(SList, nums[i] - t)
            pos2 = bisect_right(SList, nums[i] + t)
            
            if pos1 != pos2 and pos1 != len(SList): return True
            '''
             check if pos1 != len(SList), if this is the case, it means that new number is bigger than bigges number in list + t, 
             so in this case we just put it directly to our list. 
             If pos1 != pos2, this means, that we found some number i our [nums[i] - t, nums[i] + t] range, so we immediatly return True.
            '''
             
            SList.add(nums[i])
        
        return False
        
# O(n) bucket sort solution : https://leetcode.com/problems/contains-duplicate-iii/discuss/761779/Using-Bucket-dictionary-Python-Solution-greater-O(N)-time-complexity

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
	
		#edge case
        if t<0 or k<=0 or not nums:
            return False
        
        bucket={}
        width=(t+1)
        
        for i,ele in enumerate(nums):
            buck_key=(ele)//width
            
            if buck_key in bucket:
                return True
            
            else:
                bucket[buck_key]=ele
                
                if buck_key-1 in bucket and abs(ele-bucket[buck_key-1])<=t:
                    return True
                
                if buck_key+1 in bucket and abs(ele-bucket[buck_key+1])<=t:
                    return True
                
                #del leftmost element
                if i>=k:
                    #if key is not found within that window size
                    del_key=nums[i-k]//width
                    del bucket[del_key]
        return False

# Simple  Intuitive - O(n^2)

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if t == 0 and len(set(nums)) == len(nums):
            return False
        
        for i in range(len(nums)):
            for j in range(i+1, min(i+k+1, len(nums))):
                if abs(nums[i] - nums[j]) <= t:
                    return True
        return False
        
# Java TreeSet - https://leetcode.com/problems/contains-duplicate-iii/discuss/824538/Java-TreeSet-easy-to-understand-O(n-log(k))    
# Python - AVL Trees- https://leetcode.com/problems/contains-duplicate-iii/discuss/758497/Python-AVLTree-(BST)
# Python - Bucket  - https://leetcode.com/problems/contains-duplicate-iii/discuss/748483/Python3-8-line-O(N)
