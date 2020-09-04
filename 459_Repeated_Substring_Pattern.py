'''
Given a non-empty string check if it can be constructed by 
taking a substring of it and appending multiple copies of the substring together. 
You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

Example 1:

Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.
Example 2:

Input: "aba"
Output: False
'''

# fold_&_find
'''
#1. s = 'abab' 
s_fold = 'bababa'
we can find s in s_fold, where s_fold = 'bababa'

#2.  s = 'abac'
s_fold = 'bacaba'
we cannot find s in s_fold, where s_fold = 'bacaba'
'''

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        
        ss = (s + s)[1:-1]
        return ss.find(s) != -1
        
        OR
        
        s_fold = s[1:] + s[:-1]        
        return s in s_fold        
        
# O(n)
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(n//2):
            if n%(i+1)==0:
                k = int(n/(i+1))
                substr = s[:(i+1)]
                print(i+1, k, substr)
                if substr*k==s:
                    return True
        return False

# C++ 1 liner w/o KMP: return (s + s).substr(1, 2*s.size()-2).find(s) != -1;
# JAva Regex: return s.matches("^([a-z]+)\\1+$");
