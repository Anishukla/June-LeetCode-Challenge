"""
Name of the problem :- Insert Delete GetRandom O(1)
"""

class RandomizedSet:
    def __init__(self):
        self.data = {}

    def insert(self, val: int) -> bool:
        if val in self.data:
            return False
        else:
            self.data[val]=val
            return True

    def remove(self, val: int) -> bool:
        if val not in self.data:
            return False
        elif val in self.data:
            del self.data[val]
        return True

    def getRandom(self) -> int:
        r = random.randrange(len(self.data))
        return list(self.data.values())[r]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()