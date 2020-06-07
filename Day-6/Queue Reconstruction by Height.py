"""
Name of the problem :- Queue Reconstruction by Height
"""

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda p:(-p[0], p[1]))
        L = []
        
        for p in people:
            L.insert(p[1], p)
            
        return L