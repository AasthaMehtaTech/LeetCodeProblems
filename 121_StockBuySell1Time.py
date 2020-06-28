'''
Your input
[7,1,5,3,6,4]
stdout
[6, 6, 6, 6, 4, 4]

Output
5
Expected
5

'''
#simplest
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        
        buy = math.inf
        for p in prices:
            if p < buy:
                buy = p   #min price to buy the share updated
            else:
                best = max(best, p - buy)  #best profit updated
        return best

#fastest windowing//
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        windowStart = 0 
        n = len(prices)
        if not prices or n < 2:
            return 0
        
        maxProfit = 0
        for windowEnd in range(1, n):
            curProfit = prices[windowEnd] - prices[windowStart]
            if curProfit > maxProfit:
                maxProfit = curProfit
            elif prices[windowEnd] < prices[windowStart]:
                windowStart = windowEnd
                
        return maxProfit
