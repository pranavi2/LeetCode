class Solution(object):
    def isMonotonic(self, nums):
        n=len(nums)
        increasing=False
        decreasing = False

        for i in range(n-1):
            if nums[i]<nums[i+1]:
                increasing = True
            if nums[i]>nums[i+1]:
                decreasing = True

        if increasing == True and decreasing == True:
            return False
        else:
            return True

            