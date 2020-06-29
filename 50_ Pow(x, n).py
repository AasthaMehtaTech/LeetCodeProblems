#lightest
class Solution:
    def myPow(self, x: float, n: int) -> float:

        if n < 0:
            x = 1 / x
            n = -n
        po = 1
        while n:
            if n & 1:
                po *= x
            
            x *= x
            n >>= 1
        return po
        
        
#fastest
class Solution:
    @staticmethod
    
    def myPow(x: float, n: int) -> float:
        if (n == 0): return 1
        temp = Solution.myPow(x, int(n / 2))  

        if (n % 2 == 0): 
            return temp * temp 
        else: 
            if(n > 0): return x * temp * temp 
            else: return (temp * temp) / x 
