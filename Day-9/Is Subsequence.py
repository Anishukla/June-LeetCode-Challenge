"""
Name of the problem :- Is Subsequence
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        if len(s)==0:
            return True
        
        while i<len(s) and j<len(t):
            if s[i]==t[j] and i == len(s)-1:
                return True
            
            elif s[i]==t[j]:
                i = i+1
                j = j+1
                
            else:
                j = j+1
                
        return False