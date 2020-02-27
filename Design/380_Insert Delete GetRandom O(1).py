import random
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.rhash = {}
        self.rlist = []

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.rhash:
            return False
        self.rlist.append(val)
        self.rhash[val] = len(self.rlist) - 1
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.rhash:
            return False
        idx = self.rhash[val]
        self.rhash[self.rlist[-1]] = idx
        self.rlist[idx], self.rlist[-1] = self.rlist[-1], self.rlist[idx]
        self.rlist.pop()
        del self.rhash[val]

        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return random.choice(self.rlist)

obj = RandomizedSet()
obj.insert(0)
obj.insert(1)
obj.remove(0)
obj.insert(2)
obj.remove(1)
print obj.rlist
print obj.rhash