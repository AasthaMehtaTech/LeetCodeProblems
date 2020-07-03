#fast
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dicts = {}
        maxlength = start = 0
        for i,value in enumerate(s):
            if value in dicts:
                sums = dicts[value] + 1
                if sums > start:
                    start = sums
            num = i - start + 1
            if num > maxlength:
                maxlength = num
            dicts[value] = i
        return maxlength




#Simple soln by keeping track of repeated ele left index
def lengthOfLongestSubstring(self, s: str) -> int:
	i, m, d = 0, 0, {}
	for j, c in enumerate(s):
		if c in d and i <= d[c]:    # repeating character c
			m = max(m, j-i)         # i: start, j: end+1
			i = d[c]+1              # update start
		d[c] = j
	return max(m, len(s)-i)         # case end=len(s)-1


#noob
 class Solution:
 	def lengthOfLongestSubstring(self, s: str) -> int:
 		if s == '':
 			return 0
 		window = set()
 		left = 0 
 		max_len = 0
 		cur_len = 0

 		for ch in s:
 			while ch in window:
 				window.remove(s[left])
 				left += 1
 				cur_len -= 1

 			window.add(ch)
 			cur_len += 1

 			max_len = max(max_len, cur_len)

 		return max_len
