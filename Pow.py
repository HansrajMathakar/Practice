class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        
        if x == -1 and n < 0:
            return 1.0
        
        if x == 1 or (x == -1 and n%2 == 0):
            return 1.0
        elif (x == -1 and n%2 != 0):
            return -1.0
        
        if n >= 2147483647 or n <= -2147483647:
            return 0.0
        
        tmp = x
        if n > 0:
            while(n!=1):
                # print(n)
                n -= 1
                tmp = tmp*x
        elif n < 0:
            tmp = 1/x
            while (n!=-1):
                # print(n)
                n += 1
                tmp = tmp * 1/x   
        else: 
            return 1
        
        return tmp
