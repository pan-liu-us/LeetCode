# Improved Two Stacks

# Time Complexity: O(1) for all operations.
# Space Complexity: O(n)

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_tracker = [] 
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_tracker or val < self.min_tracker[-1][0]:
            self.min_tracker.append([val, 1])
        elif val == self.min_tracker[-1][0]:
            self.min_tracker[-1][1] += 1
        

    def pop(self) -> None:
        if self.min_tracker[-1][0] == self.stack[-1]:
            self.min_tracker[-1][1] -= 1
        if self.min_tracker[-1][1] == 0:
            self.min_tracker.pop()
        self.stack.pop()

        
    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_tracker[-1][0]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()