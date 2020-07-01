#mine
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix=[arr[0]]
        n=len(arr)
        for i in range(1,n):
            prefix.append(prefix[i-1]^arr[i])
        ans=[]    
        for l,r in queries:
            if l==0:
                ans.append(prefix[r])
            else:
                ans.append(prefix[l-1]^prefix[r])            
        return ans
        
#fastest
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        pre = [0]
        for num in arr:
            pre.append(pre[-1] ^ num)
        ans = list()
        for x, y in queries:
            ans.append(pre[x] ^ pre[y + 1])
        return ans        
            
            
#lightest leetcode accumulate

from itertools import accumulate
import operator

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        B = list(itertools.accumulate(arr, func=operator.xor)) + [0]
        return (B[a - 1] ^ B[b] for a, b in queries)
