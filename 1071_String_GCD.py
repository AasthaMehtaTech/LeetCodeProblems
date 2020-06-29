#
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        while str1 != str2:
            if len(str1) > len(str2):
                str1, str2 = str2, str1
            find = str2.find(str1)
            if find == -1:
                return ''
            str2 = str2[:find] + str2[find+len(str1):]
        return str2 
        
        
#like numerical gcd
    def gcdOfStrings(self, str1, str2):
        s1, s2 = str1, str2
        while s2:
            s1, s2 = s2, s1[:len(s1)%len(s2)]
        
        if s1*(len(str1)//len(s1)) == str1 and s1*(len(str2)//len(s1)) == str2:
            return s1
        return ""
        
#numerical gcd
    def gcd(a, b):
        while b:
            a, b = b, a%b
        return a
