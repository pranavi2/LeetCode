class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        reversed_str = s[::-1]
        word_length = 0
    
    
        for char in reversed_str:
            if char!= ' ':
                word_length+=1
            elif word_length>0:
                break
            
        return word_length
       