class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.input = []
        self.output = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.input.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if self.output:
            return self.output.pop()
        if self.input:
            for i in range(len(self.input)):
                self.output.append(self.input.pop())
            return self.output.pop()
        return -1

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.output:
            return self.output[-1]
        if self.input:
            for i in range(len(self.input)):
                self.output.append(self.input.pop())
            return self.output[-1]
        return -1

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if self.input or self.output:
            return False
        else:
            return True

# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
print obj.peek()
print obj.pop()
print obj.peek()
obj.push(3)
obj.push(4)
print obj.pop()
print obj.pop()
print obj.pop()
