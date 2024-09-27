class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        arr=[]
        mapping={')':'(','}':'{',']':'['}
        for char in s:
            if char in mapping:
                top_elem = arr.pop() if arr else '#'
                if mapping[char] != top_elem: 
                    return False
                else:
                    arr.append(char)
                    
        return not arr
      
# sol=Solution()      
# print(sol.isValid("("))







    



  

