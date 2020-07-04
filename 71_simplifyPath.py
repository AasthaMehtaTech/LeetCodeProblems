#https://leetcode.com/problems/simplify-path/
'''
Time complexity: O(n) - one pass through the input path for split operation and another pass through the split elements O(2n), exclude the constant -> O(n)

Space complexity: O(n) - storing the directories in the stack
'''
class Solution:
    def simplifyPath(self, path: str) -> str:
        
        if not path:
            return ""
        stack = []
        
        for i in path.split('/'):
            if i == '' or i == '.':      # if current dir (.) or empty string then continue
                continue
            if i == '..':                   # .. means goto previous dir so popout the last dir from stack, if any
                if stack:
                    stack.pop()        # then continue, we dont want to append .. in stack but just dirs
                continue
            elif i != '/':
                stack.append(i)      #append dirs to the stack

		res = '/' + '/'.join(stack)    # join dirs with '/' with a additional '/' at the begining
        return res


#fastest
class Solution:
    def simplifyPath(self, path: str) -> str:
        
        if len(path) == 0:
            return ""
            
        stack = []
        
        split_path = path.split('/')
        
        #print(split_path)
        
        ignore = { '.', '','..'}
        
        for char in split_path:
            
            #print(stack)
            
            if char not in ignore:
                stack.append(char)
            elif char == ".." and stack:
                stack.pop()
                
        
        return "/"+"/".join(stack)
