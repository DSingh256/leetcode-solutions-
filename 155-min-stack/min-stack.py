class MinStack(object):

    def __init__(self):
        self.st=[]

    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        if not self.st:
            self.st.append((value,value))
            return
        mini=min(self.getMin(), value)
        self.st.append((value, mini))

    def pop(self):
        """
        :rtype: None
        """
        self.st.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.st[-1][0]

        

    def getMin(self):
        """
        :rtype: int
        """
        return self.st[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()