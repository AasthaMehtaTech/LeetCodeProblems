#fastest
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
  ####################      
        dp = [[0] * i for i in range(1, numRows + 1)]
        dp[0][0] = 1
        for i in range(1,len(dp)):
            for j in range(len(dp[i])):
                if j == 0 or j == len(dp[i]) - 1:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
        
        return dp
        
        
        #OR
######################        
        res = [[1]]
        for _ in range(1, numRows):
            res.append(list(map(add, [0] + res[-1], res[-1] + [0])))
        return res if numRows else []
