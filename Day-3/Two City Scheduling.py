"""
Name of the problem :- Two City Scheduling
"""

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        res = sorted(costs, key = lambda sub: abs(sub[1] - sub[0]), reverse=True) 
        a = 0
        b = 0
        cost = 0
        val = len(res)
        N = val//2
        
        for i in range(val):
            if res[i][0]<res[i][1] and a<N:
                a = a+1
                cost = cost+res[i][0]
                
            elif res[i][0]>=res[i][1] and b<N:
                b = b+1
                cost = cost+res[i][1]
                
            elif res[i][0]<res[i][1] and a==N:
                b = b+1
                cost = cost+res[i][1]
                
            elif res[i][0]>=res[i][1] and b==N:
                a = a+1
                cost = cost+res[i][0]
                
        return cost