class Stack(list):
    def push(self, item):
        self.append(item)

    def peak(self):
        return self[-1]
