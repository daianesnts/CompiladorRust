class IndentStack:
    def __init__(self):
        self._stack = [0]
    
    def push(self, item):
        self._stack.append(item)
    
    def pop(self):
        if len(self._stack) > 1:
            return self._stack.pop()
    
    def peek(self):
        return self._stack[len(self._stack)-1]