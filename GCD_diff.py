'''
GCD (Greatest Common Divisor) of two positive integers is the largest positive integer that divides both numbers without a remainder.
Siblings: Nodes with the same parent are called siblings.
Level of a tree: Level of a tree is the number of edges on the longest path from the root node to a leaf.
You are given nodes of a binary tree of leven n as input.
Caluclate the GCD of each pair of siblings and then find the max & min GCD among them. Print the difference of max & min GCD ( max GCD - min GCD)

Note:
Print -1 if input tree is empty i.e level of tree is -1.
Consider those nodes which have a sibling
Print 0 if no such pair of siblings found
Input Format:
The input is in the following format:

The first line takes an integer n as input which represents the level of tree (the root node is at 0 level). (if level is equal to -1, means empty tree)
Next n+1 lines contain the nodes in the tree level order. Each i'th line represents the nodes present in the binary tree in i'th level.
1st line contains level 0 nodes. (i.e. root node).
2nd line contains nodes for level 1.
3rd line contains nodes for level 2 and so on.
Each node is represented by an integer value. Node value of -1 denotes an empty node(no node present at that place).

Output Format:
A single integer i.e., the difference of max & min GCD (max GCD - min GCD)

Constraints:
-1 <= level of tree <= 20
0 < element at nodes of tree <= 500
'''

#diff bw. max & min GCDs
class Solution(object):
        def maxDiffGCD(self, n, tree):
               if n == -1:
                   return -1
               # only root node
               if n ==  0:
                   return 0
               
               
               def findGCD(num1, num2):
                      if num2 == 0:
                          return num1
                      else:
                          return findGCD(num2,num1 % num2)
               
               
               gcds = []
               for i in range(1,n):
                     layer = tree[i]
                     for j in range(0, i * 2, 2):
                          
                          num1 = max(layer[j], layer[j+1])
                          num2 = min(layer[j], layer[j+1])
                          
                          if num1 == -1 or num2 == -1:
                             continue
                          else:
                             gcd = findGCD(num1,num2)
                          
                          if not gcds:
                              gcds.append(gcd)
                          elif gcd < gcds[0]:
                              gcds = [gcd] + gcds
                          elif gcd > gcds[-1]:
                              gcds.append(gcd)
                          else:
                              gcds = gcds[:-1] + [gcd] + gcds[-1]
          
          return gcds[-1] -  gcds[0] 
                       
