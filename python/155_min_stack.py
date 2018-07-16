from queue import PriorityQueue

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minheap = PriorityQueue()

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        self.minheap.put(x)        

    def pop(self):
        """
        :rtype: void
        """
        if self.stack:
            elem = self.stack.pop()
            if elem == self.minheap.queue[0]:
                self.minheap.get()
            return elem        

    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if not self.minheap.empty():
            return self.minheap.queue[0]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()