class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        t = self.trie
        for c in word:
            t = t.setdefault(c, {})
        t["end"] = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        t = self.trie
        for c in word:
            if c not in t:
                return False
            t = t[c]
        return "end" in t

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        t = self.trie
        for c in prefix:
            if c not in t:
                return False
            t = t[c]
        return True

# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert('stone')
obj.insert('switch')
print obj.trie