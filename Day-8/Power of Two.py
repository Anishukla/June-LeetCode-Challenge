"""
Name of the problem :- Power of Two
"""

import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return False
        else:
            val = math.log2(n)        
            if int(val)==val:
                return True
            else:
                return False