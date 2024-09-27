class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romanArr={
             'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
        }
        total=0
        prev_val=0
        for char in reversed(s):
            currentVal= romanArr[char]
            if currentVal < prev_val:
                total-=currentVal
            else:
                total+=currentVal
            
            prev_val = currentVal
        return total
# sol=Solution()
# print(sol.romanToInt('III'))                



