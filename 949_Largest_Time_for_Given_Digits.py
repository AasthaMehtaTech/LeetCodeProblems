
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

#fastest
class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        
        str_A = [str(x) for x in A]
        max_hour = [ str(x) for x in range(23,9,-1)]
        max_zero = ["0"+ str(y) for y in range(9,-1,-1)]
        hours = max_hour + max_zero 
        max_minutes = ["5","4","3","2","1","0"]
        
        final_str = ""
        for hour in hours:
            cpy = [x for x in str_A] 
            if hour[0] in cpy:
                cpy.remove(hour[0])
            
                if hour[1] in cpy:
                    final_str = hour[0]+hour[1]     
                    cpy.remove(hour[1])
                
                    for min_ in max_minutes: 
                        if min_ in cpy:
                            cpy.remove(min_)
                            final_str = final_str + ":" + min_ + cpy[0]
                            return final_str                                
        return ""
    
#zipping
class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        largest_time, max_mins = '', -1
        
        for p in itertools.permutations(A):
            hours = p[0]*10 + p[1]
            minutes = p[2]*10 + p[3]
            
            if hours < 24 and minutes < 60:
                total_mins = hours*60 + minutes
                
                if total_mins > max_mins:
                    max_mins = total_mins
                    largest_time = '{}{}:{}{}'.format(*p)
        return largest_time

#without permu library
class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        totalString = "".join(str(i) for i in A)
        ways = [-1]
        self.getPerm("", totalString, ways)
        print(ways)
        return "" if ways[-1] == -1 else str(ways[-1])[:2] + ":" + str(ways[-1])[2:]
        
    def getPerm(self, start, rest, ways):
        if len(start) == 4:
            if (self.isValid(start)):
                ways.append(start)
                if int(start) < int(ways[-2]):
                    ways[-1], ways[-2] = ways[-2], ways[-1]
        else:
            for i in range(len(rest)):
                other = rest[:i] + rest[i+1:]
                self.getPerm(start+rest[i], other, ways)
            
#dfs
class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        times = []
        def dfs(A = A, curr = []):
            if len(A) == 0:
                time = (10*curr[0]+curr[1], 10*curr[2]+curr[3])
                if time[0] < 24 and time[1] < 60:
                    times.append(time)                    
        
    def isValid(self, num):
        a, b = num[:2], num[2:]
        return 0 <= int(a) < 24 and 0 <= int(b) < 60
                return
            for i in range(len(A)):
                temp = A[:i] + A[i+1:]
                dfs(temp, curr + [A[i]])
        dfs()
        if len(times) == 0:
            return ""
        times.sort()
        biggest = times[-1]
        time = ""
        if biggest[0] == 0:
            time += "00"
        elif biggest[0] < 10:
            time += "0" + str(biggest[0])
        else:
            time += str(biggest[0])
        time += ":"
        if biggest[1] == 0:
            time += "00"
        elif biggest[1] < 10:
            time += "0" + str(biggest[1])
        else:
            time += str(biggest[1])
        return time
