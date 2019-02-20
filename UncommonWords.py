
class Solution:
    def uncommonFromSentences(self, A: 'str', B: 'str') -> 'List[str]':
        d = dict()
        c = 1
        res = []
        for w in A.split(' '):
            d[w] = d.get(w, 0) + 1
            
        for w in B.split(' '):
            d[w] = d.get(w, 0) + 1
            
        for i in d.keys():
            if d[i] == 1:
                res.append(i)
        
        return res
        
