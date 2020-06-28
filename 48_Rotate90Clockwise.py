#fastest
        n = len(matrix)

        for i in range(n // 2):
            for j in range(n - n // 2):
                matrix[j][n - 1 - i], matrix[n - 1 - i][n - 1 - j], matrix[n - 1 - j][i], matrix[i][j] \        
                = matrix[i][j], matrix[j][n - 1 -i], matrix[n - 1 - i][n - 1 - j], matrix[n - 1 - j][i]
                
                
# basic- transpose matrix, reverse each row     
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # transpose
        for i in range(n):
            for j in range(i + 1, n):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp
        # flip horizontally
        for i in range(n):
            for j in range(n // 2):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[i][n - 1 - j]
                matrix[i][n - 1- j] = tmp
            
