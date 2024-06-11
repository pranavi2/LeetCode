class Solution(object):
    def reverse(self, x):
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        rev=0

        negative=x<0
        x=abs(x)

        while x!=0:
            digit=x%10
            x//=10

            if rev> (INT_MAX - digit)//10:
                return 0
            rev=rev*10+digit

        if negative:
            rev=-rev

            if rev<INT_MIN:
                return 0
        return rev

       
       