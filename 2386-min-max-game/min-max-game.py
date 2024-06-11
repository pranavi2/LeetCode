class Solution(object):
    def minMaxGame(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        while len(nums) > 1:
            newNums = []
            for i in range(len(nums) // 2):
                if i % 2 == 0:
                    newNums.append(min(nums[2 * i], nums[2 * i + 1]))
                else:
                    newNums.append(max(nums[2 * i], nums[2 * i + 1]))
            nums = newNums
        return nums[0]
        
       
                
           
                
            
       
    