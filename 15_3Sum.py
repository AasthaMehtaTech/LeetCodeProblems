class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        for comb in itertools.combinations(nums, 3):
            if sum(comb) == 0:
                results.append(comb)
        return list(set(tuple(sorted(res)) for res in results))
 
# -----------------------------------------------------------------

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

# -----------------------------------------------------------------

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=set()
        tab={}
        pos,neg=set(),set()
        for n in nums:
            if n not in tab:
                tab[n]=1
            else: tab[n]+=1
            if n>=0: pos.add(n)
            if n<=0: neg.add(n)
        for i in pos:
            for j in neg:
                tar=-i-j
                if tar in tab and tab[tar]>=sum(x==tar for x in [i,j,-i-j]):
                    res.add(tuple(sorted([i,j,-i-j])))
        return res
# -----------------------------------------------------------------

# Othersss
class Solution:
  def threeSum(self, nums: List[int]) -> List[List[int]]:
    return self.fast(nums)

  # O(n^{2-e})
  def fast(self, nums: List[int]) -> List[List[int]]:
    if len(nums) < 3 or min(nums) > 0 or max(nums) < 0: # O(n)
        return []
    res = []
    count = defaultdict(int)
    for num in nums: # O(n)
        count[num] += 1
    nums = sorted(count) # O(n log n)
    for idx, num in enumerate(nums): # O(n - e)
        if num > 0:
            break
        two_sum = -num
        num2_min, num2_max = two_sum - nums[-1], two_sum / 2
        i = bisect_left(nums, num2_min, idx + 1) # O(log n)
        j = bisect_left(nums, num2_max, i) # O(log n)
        for num2 in nums[i:j]: # O(??)
            num3 = two_sum - num2
            if num3 in count:
                res.append((num, num2, num3))
    for num in nums: # O(n)
        if count[num] > 1:
            if num == 0 and count[num] >= 3:
                res.append((num, num, num))
            elif num != 0 and 0 - 2 * num in count:
                res.append((num, num, 0 - 2 * num))
    return res
  

  # time O(n^3), space O(n^3)
  def brute(self, nums: List[int]) -> List[List[int]]:
    results = set()
    for i, n1 in enumerate(nums[:-2]):
      for j, n2 in enumerate(nums[i + 1:-1]):
        for n3 in nums[i + j + 2:]:
          if n1 + n2 + n3 == 0:
            results.add(tuple(sorted([n1, n2, n3])))
    return results      
