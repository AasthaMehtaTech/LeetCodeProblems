
'''
Given an array of 4 digits, return the largest 24 hour time that can be made.
The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from 00:00, a time is larger if more time has elapsed since midnight.
Return the answer as a string of length 5.  If no valid time can be made, return an empty string.

Input: [1,2,3,4]
Output: "23:41"

Input: [5,5,5,5]
Output: ""
'''
backtracking: https://leetcode.com/problems/subsets/discuss/27281/A-general-approach-to-backtracking-questions-in-Java-(Subsets-Permutations-Combination-Sum-Palindrome-Partitioning)

Permutations:

#simple reverse sort eligibility check

from itertools import permutations
class Solution:                                  
    def largestTimeFromDigits(self, A: List[int]) -> str:
        combinations_arr = list(permutations(sorted(A, reverse=True)))        
        for h1, h2, m1, m2 in combinations_arr:
            if h1 * 10 + h2 < 24 and m1 * 10 + m2 < 60:
                return f'{h1}{h2}:{m1}{m2}'
        return ''

# 1-liner     
     
return ''.join(result[-1]) 
              if (result := sorted([[*p[:2]]+[':']+[*p[2:]] 
                                      for p in itertools.permutations([str(n) for n in A])
                                        if int(''.join(p[:2])) < 24 and int(''.join(p[2:])) < 60],
                             key=lambda p: int(''.join(p[:2]))*100 + int(''.join(p[3:]))
                             )
               )
              else ""     


'''
#cpp condition check asc

class Solution {
public:
    string largestTimeFromDigits(vector<int>& A) {
        string ans = "";
        sort(A.begin(),A.end());
        do{
            if((A[0]==2 && A[1]<=3 || A[0]<2) && A[2]<=5)
                ans = to_string(A[0])+to_string(A[1])+":"+to_string(A[2])+to_string(A[3]);
        }while(next_permutation(A.begin(),A.end()));
        return ans;
    }
};
'''
