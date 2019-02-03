class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        # print(len(A))
        # print(len(B))
        
        difference = (sum(B)-sum(A))//2
        set_A = set(A)
        set_B = set(B)
        for element in set_A:
            if element + difference in set_B:
                return [element, element + difference]
