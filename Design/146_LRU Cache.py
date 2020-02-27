class DNode(object):
    def __init__(self, value, key=None, next=None, pre=None):
        self.key = key
        self.value = value
        self.next = next,
        self.pre = pre



class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capcity = capacity
        self.map = {}
        self.head = DNode(None)
        self.tail = self.head
        self.exist = 0

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        curNode = self.map.get(key)
        if curNode:
            tailNode = self.tail
            if curNode != tailNode:
                curNode.next.pre = curNode.pre
                curNode.pre.next = curNode.next
                tailNode.next = curNode
                curNode.next, curNode.pre = None, tailNode
                self.tail = curNode
            ret = curNode.value
        else:
            ret = -1
        return ret

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if self.capcity == 0:
            return False
        if key in self.map:
            curNode = self.map.get(key)
            tailNode = self.tail
            if curNode != tailNode:
                curNode.next.pre = curNode.pre
                curNode.pre.next = curNode.next
                tailNode.next = curNode
                curNode.next, curNode.pre = None, tailNode
                self.tail = curNode
            curNode.value = value
        else:
            curNode = DNode(value, key, None, None)
            curNode.next, curNode.pre = None, self.tail
            self.tail.next = curNode
            self.tail = curNode
            self.exist += 1
            self.map[key] = curNode
            if self.exist == 1:
                self.head.next = curNode
            if self.exist > self.capcity:
                headNode = self.head.next
                self.map.pop(headNode.key)
                self.head.next = headNode.next
                self.head.next.pre = self.head

