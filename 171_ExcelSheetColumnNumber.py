#simple yet slow
class Solution:
    def __init__(self):
        
        self.d= dict( (key, i) for i, key in enumerate(string.ascii_uppercase,1) )
    
    def titleToNumber(self, s: str) -> int:
        n=len(s)
        ans=0
        for i,char in zip(range(n-1, -1, -1), s):
            ans+=(26**i)*self.d[char]
            
        return ans   
        
        
        """
        def enumerate2(xs, start=0, step=1):
        for x in xs:
            yield (start, x)
            start += step
        """
        
#fast & light
class Solution:
    def titleToNumber(self, s: str) -> int:
        res = 0
        for char in s:
            res *= 26
            res += (ord(char)-ord('A'))+1
        return res
    
    
#another light
class Solution:
    def titleToNumber(self, s: str) -> int:
        res = 0
        nums = [ord(ch) - ord('A') + 1 for ch in s]
        for n in nums:
            res = res * 26 + n
        return res
