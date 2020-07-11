#2 sum 
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSumII(nums, i, res)
        return res

    def twoSumII(self, nums, i: int, res):
        lo, hi = i + 1, len(nums) - 1
        while (lo < hi):
            sum = nums[i] + nums[lo] + nums[hi]
            if sum < 0 or (lo > i + 1 and nums[lo] == nums[lo - 1]):
                lo += 1
            elif sum > 0 or (hi < len(nums) - 1 and nums[hi] == nums[hi + 1]):
                hi -= 1
            else:
                res.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                hi -= 1

#partition fastest
class Solution:
    def threeSum(self,n):
        f={}
        for i in n:f[i]=f.get(i,0)+1        
        n=sorted(f)
        a=[]        
        for i,I in enumerate(n):
            if not I:
                if f[I]>2:a.append((0,0,0))
            elif f[I]>1 and -2*I in f:a.append((I,I,-2*I))    
            if I<0:
                t=-I
                l=bisect_left(n,t-n[-1],i+1)
                r=bisect_right(n,t//2,l)
                for J in n[l:r]:
                    K=t-J
                    if K in f and K!=J:a.append((I,J,K))
        return a
        
        
#inbuilt counter
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        counter = collections.Counter(nums)
        nums = sorted(counter)
        ret = []
        for i, num in enumerate(nums):
            # case i. three numbers are the same - [0,0,0]
            if num==0:
                if counter[num] > 2:
                    ret.append([0, 0, 0])
            # case ii. two numbers are the same
            elif counter[num] > 1 and -2 * num in counter:
                ret.append([num, num, -2 * num])
            # case iii. not any of the three numbers are the same
            if num < 0:
                opposite = -num
                left = bisect_left(nums, opposite - nums[-1], i + 1)
                right = bisect_right(nums, opposite / 2, left)
                for a in nums[left:right]:
                    b = opposite - a
                    if b in counter and a!=b:
                        ret.append([num, a, b])
        return ret
        
#maths
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ret = []
        for i, n1 in enumerate(nums[:-2]):
            if n1 > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                n2, n3 = nums[l], nums[r]
                total = n1 + n2 + n3
                if total < 0 or (i + 1 < l and nums[l] == nums[l-1]):
                    l += 1
                elif total > 0 or (r < len(nums)-1 and nums[r] == nums[r+1]):
                    r -= 1
                else:
                    ret.append([n1, n2, n3])
                    l += 1
                    r -= 1
        return ret

#3 pointers approach
def threeSum(self, nums: List[int]) -> List[List[int]]:
		# Sort in increasing order
        nums.sort()
        res = []
        # For every nums[i], find out two numbers between j and k such that all adds to 0
		# [i, j, k] --> [0, 1, n], [1, 2, n], [1, 3, n], ..... [n, n+1, n] 
        for i in range(len(nums)):
            # Avoid duplicates
            if i>0 and nums[i]==nums[i-1]: continue
            # Two pointers j and k
            j = i+1
            k = len(nums)-1
            # Target value
            _sum = 0-nums[i]
            # Find two numbers between j and k that adds to target value
            while j<k:
                if nums[j]+nums[k] == _sum:
                    res.append([nums[i],nums[j],nums[k]])
                    # Avoid duplicates (alternative: return set(res))
                    while j<k and nums[j]==nums[j+1]: j+=1
                    while j<k and nums[k]==nums[k-1]: k-=1
                    j+=1
                    k-=1
                elif nums[j]+nums[k] < _sum:
                    j+=1
                else:
                    k-=1
        return res
