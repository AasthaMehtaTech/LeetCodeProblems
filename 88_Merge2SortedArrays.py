class Solution:
    def merge(self, A, m, B, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m-1
        j = n-1
        index = m+n-1
        
        while i>=0 and j>=0:
            if A[i] > B[j]:
                A[index] = A[i]
                i-=1
            else:
                A[index] = B[j]
                j-=1
            index-=1
        
        
        while i>=0:
            A[index] = A[i]
            i-=1
            index-=1
        
        while j>=0:
            A[index] = B[j]
            j-=1
            index-=1
