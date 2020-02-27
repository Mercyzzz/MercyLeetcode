from queue import Queue
class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.input = Queue()
        self.output = Queue()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.input.put(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if not self.output.empty():
            return self.output.get()
        while not self.input.empty():
            self.output.put(self.input.get())
        return self.output.get()


    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if not self.output.empty():
            return self.output.get()
        while not self.input.empty():
            self.output.put(self.input.get())
        return self.output.get()

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """

# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
print obj.pop()
