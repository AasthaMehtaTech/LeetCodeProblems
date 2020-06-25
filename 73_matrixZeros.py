#fastest
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        if rows > 0:
            cols = len(matrix[0])
        rowChange = set()
        colChange = set()
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    rowChange.add(row)
                    colChange.add(col)
        
        for row in rowChange:
            matrix[row] = [0] * cols
        
        for row in range(rows):
            for col in colChange:
                matrix[row][col] = 0
