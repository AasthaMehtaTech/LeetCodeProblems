#https://leetcode.com/discuss/interview-question/762854/Amazon-or-Onsite-question-2020-Rejected
#similar to growth of life/ rotten orange problems on leetcode.
#Question :
'''
Given a room represented like a grid, you have to escape from the fire. 
The grid looks like the following where 
0 represents empty place you can move through,
1 represents you (a person) and
2 represents fire. You can consider yourself escaped if you reach any of the sides that's not on fire
(ie., grid[i][j]!=2 && i = 0 || j == 0 || i == m-1 || j == n-1 where 0<=i<m , 0 <=j<n and m,n being length and height of the grid).
Goal is to find the shortest distance from 1 to any of the sides. I was able to solve this with plain BFS.

Followup:
Now for every step you take, the fire grows a step in all four directions. 
'''

from collections import deque
class Solution:
    def forest_fire(self, grid):
        m = len(grid); n = len(grid[0])
        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.appendleft((i, j)) # All unsafe cells should be branched out before any safe cell at the same level 
                    # to ensure at a certain level fire hasn't already reached where a person wants to be.
                elif grid[i][j] == 1:
                    queue.append((i, j)) # Append at right end
        
        dist = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                i, j = queue.popleft()
                if grid[i][j] == 1 and (i==0 or i == m-1 or j == 0 or j == n-1):
                    return dist # reached the boundary

                for x, y in [(i+1,j), (i,j+1), (i-1,j), (i,j-1)]:
                    if 0<=x<m and 0<=y<n and grid[x][y] == 0:
                        queue.append((x,y))
                        grid[x][y] = 2 if grid[i][j] == 2 else 1
            dist += 1
            
        return -1 # if there is no way out of the forest and you die 
