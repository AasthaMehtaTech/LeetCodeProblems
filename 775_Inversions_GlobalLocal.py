'''
We have some permutation A of [0, 1, ..., N - 1], where N is the length of A.

The number of (global) inversions is the number of i < j with 0 <= i < j < N and A[i] > A[j].

The number of local inversions is the number of i with 0 <= i < N and A[i] > A[i+1].

Return true if and only if the number of global inversions is equal to the number of local inversions.

Example 1:

Input: A = [1,0,2]
Output: true
Explanation: There is 1 global inversion, and 1 local inversion.
Example 2:

Input: A = [1,2,0]
Output: false
Explanation: There are 2 global inversions, and 1 local inversion.
'''


#approach 1 simple to understand
class Solution:
    def isIdealPermutation(self, a: List[int]) -> bool:
        for i in range(len(a)):
            if not (a[i]==i or a[i]==i+1 or a[i]==i-1):
                return False    
        return True

#approach 2
        if not A: return
        for i, x in enumerate(A):
            if abs(x-i) > 1:
                return False
        return True
        
        
        #OR Similar to fastest
        
        for i in range(len(A)):
            if abs(A[i] - i) > 1:
                return False
        return True
        
        #OR
        
        return all(abs(A[i]-i) <= 1 for i in range(len(A)))
        
        #or
        
        #return false when find a non-local inversion
        for i in range(len(A)):
            for j in range(i+2, len(A)):
                if (A[i] > A[j]): return False
        return True
 

#approach 3
max_idx = 0
for i in range(2, len(A)):
	if A[i] < A[max_idx]:
		return False
	if A[i - 1] > A[max_idx]:
		max_idx = i - 1
return True
