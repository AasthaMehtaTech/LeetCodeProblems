'''
Example 1:

Input: satisfaction = [-1,-8,0,5,-9]
Output: 14
Explanation: After Removing the second and last dish, the maximum total Like-time coefficient will be equal to (-1*1 + 0*2 + 5*3 = 14). Each dish is prepared in one unit of time.
Example 2:

Input: satisfaction = [4,3,2]
Output: 20
Explanation: Dishes can be prepared in any order, (2*1 + 3*2 + 4*3 = 20)
Example 3:

Input: satisfaction = [-1,-4,-5]
Output: 0
Explanation: People don't like the dishes. No dish is prepared.
Example 4:

Input: satisfaction = [-2,5,-1,0,3,-3]
Output: 35
'''


#awice one liner- O(nlogn)
 
 return max(0, max(itertools.accumulate(itertools.accumulate(sorted(arr, reverse=True)))))


#mine- 36/132/ ms

class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        n=len(satisfaction)
        ans=[]
        
        for j in range(n):
            ans.append(sum([i*a for i,a in enumerate(satisfaction[j:],1)]))
        
        return max(max(ans),0)

#fastest 16 ms
    def maxSatisfaction(self, satisfaction):
        satisfaction = sorted(satisfaction)
        slen = len(satisfaction)
        if satisfaction[slen-1] <= 0:
            return 0
        start = -1
        for i in range(slen):
            if satisfaction[i] >= 0:
                start = i
                break
        ans = 0
        cur = 0
        suffix = 0
        for i in range(slen-1, -1, -1):
            suffix += satisfaction[i]
            cur += suffix
            if cur > ans:
                ans = cur
            else:
                break

        return ans
        
        
#24 ms Check
class Solution:
    def maxSatisfaction(self, arr: List[int]) -> int:
        arr.sort(reverse=True)
        ret = 0
        raw = 0
        for v in arr:
            if ret + v + raw > ret:
                ret += v + raw
                raw += v
        return ret
        
#36 ms
class Solution:
    def maxSatisfaction(self, A: List[int]) -> int:
        
        res = total = 0
        A.sort()
        while A and A[-1] + total > 0:
            total += A.pop()
            res += total
        return res
