#fastest
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if intervals == []:
            return []
        intervals.sort(key=lambda x: x[0])
        curr_low, curr_high = intervals[0]
        result = []
        for low, high in intervals[1:]:
            if low > curr_high:
                result.append([curr_low, curr_high])
                curr_low, curr_high = low, high
            else:
                curr_high = max(curr_high, high)
        result.append([curr_low, curr_high])
        return result
        
        
#lightest
class Solution:
    def merge(self, e: List[List[int]]) -> List[List[int]]:
        res=[]              
        for i in sorted(e,key=lambda x:x[0]):             
            if res and res[-1][1]>=i[0]:
                res[-1][1]=max(res[-1][1],i[1])
            else:
                res.append(i)  
        return res
