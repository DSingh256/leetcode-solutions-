class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        
        n1=str(n)        
        
        while True:
            a=1
            for i in n1:
                a=a*int(i)
            if a% t == 0:
                return n
            n+=1
            n1=str(n)
       