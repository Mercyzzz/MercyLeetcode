from Queue import PriorityQueue


class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minPQ = PriorityQueue()
        self.maxPQ = PriorityQueue()

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """


        self.minPQ.put(num)
        self.maxPQ.put(-self.minPQ.get())
        if self.minPQ.qsize() < self.maxPQ.qsize():
            self.minPQ.put(-self.maxPQ.get())

    def findMedian(self):
        """
        :rtype: float
        """
        if self.minPQ.empty() and self.maxPQ.empty():
            return 0
        if self.minPQ.qsize() > self.maxPQ.qsize():
            return self.minPQ.queue[0]
        else:
            return (self.minPQ.queue[0] - self.maxPQ.queue[0]) / 2.0

# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(2)
obj.addNum(3)
obj.addNum(4)
print obj.findMedian()
